#!/usr/bin/env python3

PRJVER = "1.0"

# Helper script for Windows kernel debugging with IDA Pro on native Bochs debugger
# https://github.com/therealdreg/windbgtocstruct
# GNU General Public License v3.0
#
# By Aidan Khoury (dude719)
# Twitter @aidankhoury
# https://github.com/ajkhoury/Windbg2Struct
#
# Mod by David Reguera Garcia aka Dreg
# Twitter @therealdreg
# https://www.fr33project.org
# dreg@fr33project.org
# https://github.com/therealdreg
#
# 2022/10/07 by Dreg
#   - project renamed to windbgtocstruct.py
#   - ported to python3
#   - code style fixed using black (python -m black windbgtocstruct.py)
#   - added changelog
#   - added some prints
#   - comestic changes (new header...)
#   - added python3 shebang
#   - fixed bugs
#   - Dummy structs
#   - pragma packs
#   - sizeof support
#   - included input as C comment
#   - Convert anonymous unions/struct to a named version. ISO C90 doesn’t support unnamed structs/unions.
#
# WARNING: BULLSHIT CODE x)
#

import sys

SIZEST = "0"

def printf(format, *args):
    sys.stdout.write(format % args)


key_types = {
    "UChar": "UCHAR",
    "Char": "CHAR",
    "Wchar": "WCHAR",
    "Uint2B": "USHORT",
    "Uint4B": "ULONG",
    "Uint8B": "ULONG64",
    "Int2B": "SHORT",
    "Int4B": "LONG",
    "Int8B": "LONG64",
    "Void": "VOID",
}


def get_input(prompt):
    print(prompt)
    lines = []
    line = input()
    while line != "":
        line = line.replace("\t", "")
        lines.append(line)
        line = input()
    lines = "".join(lines)
    return lines


def get_struct_name(dt_dump):
    exclamation_idx = dt_dump.index("!")
    first_addition_idx = dt_dump.index("+")
    structname = dt_dump[exclamation_idx + 1 : first_addition_idx]
    return structname.strip()


def get_fields(dt_dump):
    """Returns generated field list"""
    field_list = []

    first_addition_idx = dt_dump.index("+")
    s = dt_dump[first_addition_idx + 1 :]
    s = s.split("+")

    for field in s:
        current_field = {
            "name": "",
            "type": "",
            "pointer": 0,
            "offset": -1,
            "size": 0,
            "array_sizes": [],
            "union": False,
            "bit_pos": -1,
        }

        offset_end_idx = field.index(" ")
        current_field["offset"] = int(field[:offset_end_idx], 16)

        field = field[offset_end_idx + 1 :]
        name, dtype = field.split(":")
        # strip leading and trailing whitespace
        name = name.strip()
        dtype = dtype.strip()

        current_field["name"] = name

        # Bitfield type
        if "Pos " in dtype:
            dtype = dtype.strip(" ")
            pos, bit = dtype.split(",")
            current_field["bit_pos"] = int(pos[3:])
            current_field["size"] = int(bit[: bit.index("B")])

        # Array field type
        elif "[" in dtype:
            dtlist = dtype.split(" ")
            for dt in dtlist:
                if "[" in dt:
                    arr = dt.strip("[]")  # drop the brackets
                    current_field["array_sizes"].append(int(arr))
                elif "Ptr64" in dt:
                    current_field["pointer"] += 1
                elif "Ptr32" in dt:
                    current_field["pointer"] += 1
                else:
                    current_field["type"] = dt

        # Pointer field type
        elif "Ptr64" or "Ptr32" in dtype:
            dtlist = dtype.split(" ")
            for dt in dtlist:
                if "Ptr64" in dt:
                    current_field["pointer"] += 1
                else:
                    current_field["type"] = dt

        # Regular field type
        else:
            current_field["type"] = dtype

        # Finalize data for the previous field
        if len(field_list) > 0:
            if field_list[-1]["bit_pos"] == -1 and current_field["bit_pos"] == -1:
                # Calculate the previous field's size by subtracting the
                # current offset from the previous offset
                field_list[-1]["size"] = (
                    current_field["offset"] - field_list[-1]["offset"]
                )
                # print(field_list[-1]['size'])
            # check if the previous or current field is a union
            elif (
                field_list[-1]["bit_pos"] != -1
                and current_field["bit_pos"] == -1
                and field_list[-1]["offset"] == current_field["offset"]
            ):
                current_field["union"] = True
            elif (
                field_list[-1]["bit_pos"] == -1
                and field_list[-1]["offset"] == current_field["offset"]
            ):
                field_list[-1]["union"] = True

        # Append the field to the list
        field_list.append(current_field)

    return field_list


#def union_size(union_field):
#    total = 0
#    for field in fields:
#        if field["union"] == False and field["offset"] == union_field["offset"]:
#            total = total + field["size"]
#    return total


def find_union_header(fields, union_field):
    for field in fields:
        if field["union"] == True and field["offset"] == union_field["offset"]:
            return field
    return 0


def print_bitfield(bit_field, bit_field_type):
    printf(
        "\t%s %s : %d; // 0x%X\n",
        bit_field_type,
        bit_field["name"],
        bit_field["size"],
        bit_field["offset"],
    )

LAST_ANON_NR = 0
def print_union(fields, union_field):
    global LAST_ANON_NR 
    LAST_ANON_NR= LAST_ANON_NR + 1
    completed_fields = []
    union_header = find_union_header(fields, union_field)
    if union_header != 0:
        printf("\tunion "  + "aNoN_" + str(LAST_ANON_NR) + "\n\t{\n")
        LAST_ANON_NR= LAST_ANON_NR + 1
        if union_header["type"] in key_types:
            if union_header["pointer"] > 0:
                printf("\t\tP%s", key_types[union_header["type"]])
                for _ in range(union_header["pointer"] - 1):
                    printf("*")
                printf(" %s; // 0x%X\n", union_header["name"], union_header["offset"])
            else:
                printf(
                    "\t\t%s %s; // 0x%X\n",
                    key_types[union_header["type"]],
                    union_header["name"],
                    union_header["offset"],
                )
        else:
            if union_header["pointer"] > 0:
                printf("\t\t%s", union_header["type"])
                for _ in range(union_header["pointer"]):
                    printf("*")
                printf(" %s; // 0x%X\n", union_header["name"], union_header["offset"])
            else:
                printf(
                    "\t\t%s %s; // 0x%X\n",
                    union_header["type"],
                    union_header["name"],
                    union_header["offset"],
                )
        printf("\t\tstruct " + "aNoN_" + str(LAST_ANON_NR) + "\n\t\t{\n")
        LAST_ANON_NR= LAST_ANON_NR + 1
        for field in fields:
            if (
                field["union"] == False
                and field["bit_pos"] != -1
                and field["offset"] == union_header["offset"]
            ):
                printf("\t\t")
                if union_header["type"] in key_types:
                    print_bitfield(field, key_types[union_header["type"]])
                else:
                    print_bitfield(field, union_header["type"])
                completed_fields.append(field)
        printf("\t\t} " + "aNoN_" + str(LAST_ANON_NR) + ";\n\t}")
        LAST_ANON_NR= LAST_ANON_NR + 1
        printf(" " + "aNoN_" + str(LAST_ANON_NR) + ";\n")
        LAST_ANON_NR= LAST_ANON_NR + 1
    else:
        printf("\tstruct " + "aNoN_" + str(LAST_ANON_NR) + "\n\t{\n")
        bit_field_type = "ULONG"
        bit_fields_sum = 0
        bit_fields = []
        for field in fields:
            if field["bit_pos"] != -1 and field["offset"] == union_field["offset"]:
                bit_fields.append(field)
                bit_fields_sum += field["size"]
                completed_fields.append(field)
        # Get type based on sum of bits
        if bit_fields_sum > 32:
            bit_field_type = "ULONGLONG"
        elif bit_fields_sum > 16:
            bit_field_type = "ULONG"
        elif bit_fields_sum > 8:
            bit_field_type = "USHORT"
        else:
            bit_field_type = "UCHAR"
        # Dump the bitfields
        for bit_field in bit_fields:
            printf("\t")
            print_bitfield(bit_field, bit_field_type)
        printf("\t} " +  "aNoN_" + str(LAST_ANON_NR) + ";\n")
        LAST_ANON_NR= LAST_ANON_NR + 1
    return completed_fields


def generate_struct(dt_dump):
    # Main structure genertation method
    struct_name = get_struct_name(dt_dump)
    fields = get_fields(dt_dump)
    union_fields_completed = []

    print('''
#include <Windows.h>
#pragma pack(push)
#pragma pack(1)
''')

    print("#define SIZEOF_" + struct_name + " " + SIZEST + "\n")

    printf("typedef struct %s\n{\n", struct_name)

    # Need to use this eventually for nested structs maybe.
    # Would be better to create struct list in the get_fields function
    previous_field = None
    dummy_structs = []
    next_index = 0
    drgdict = {} 
    for field in fields:
        next_index = next_index + 1
        # print out the type
        if field["bit_pos"] != -1:
            if not any(
                union_field["offset"] == field["offset"]
                for union_field in union_fields_completed
            ):
                union_fields_completed.extend(print_union(fields, field))
        elif field["union"] == True:
            # skip as its handled in print_union
            continue
        else:
            if field["type"] in key_types:
                if field["pointer"] > 0:
                    printf("\tP%s", key_types[field["type"]])
                    for _ in range(field["pointer"] - 1):
                        printf("*")
                else:
                    printf("\t%s", key_types[field["type"]])
            else:
                if field["type"][0] == "_":
                    printf("\tstruct %s", field["type"])
                    if field["pointer"] > 0:
                        size_ar = "1"
                    else:
                        try:
                            size_ar = str(fields[next_index]["offset"] - field["offset"])
                        except IndexError:
                            size_ar = "1" 
                    if field["type"] not in drgdict:
                        dummy_structs.append("struct " + field["type"] + "\n" + "{\n" + "\tUCHAR data[" + size_ar + "];" + "\n};\n")
                        drgdict[field["type"]] = 1
                else:
                    printf("\t%s", field["type"])
                if field["pointer"] > 0:
                    for _ in range(field["pointer"]):
                        printf("*")

            printf(" %s", field["name"])
            if field["array_sizes"]:
                for arr_size in field["array_sizes"]:
                    printf("[%d]", arr_size)
            printf("; // 0x%X\n", field["offset"])

        # To be used eventually for nested structs (maybe)
        previous_field = field

    struct_name = struct_name[1:]
    printf("} %s, *P%s;\n", struct_name, struct_name)

    if len(dummy_structs):
        print("\n// Dummy structs:")
    for dummy_struct in dummy_structs:
        print(dummy_struct)

    print('''
#pragma pack(pop)
''')


def main():
    global SIZEST
    global PRJVER

    print("version: " + PRJVER)

    print(
        """
 windbgtocstruct
 https://github.com/therealdreg/windbgtocstruct
 GNU General Public License v3.0
 -
 Mod by David Reguera Garcia aka Dreg
 Twitter @therealdreg
 https://www.fr33project.org
 dreg@fr33project.org
 https://github.com/therealdreg    
 -
 Based from Windbg2Struct By Aidan Khoury (dude719)
 Twitter @aidankhoury
 https://github.com/ajkhoury/Windbg2Struct
"""
    )

    if len(sys.argv) > 1:
        SIZEST = sys.argv[1]

    print("/*")
    dt_dump = get_input("Enter dumped WinDbg data-type: ")
    print("*/")
    if dt_dump:
        generate_struct(dt_dump)
    else:
        print("Error: invalid input")
    return


if __name__ == "__main__":
    main()
