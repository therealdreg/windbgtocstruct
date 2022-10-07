# windbgtocstruct
Helper Script to convert a Windbg dumped structure (using the 'dt' command) into a C structure. It creates dummy structs for you if needed.

```
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
```

If you don't need all the sub/structures defined in your headers, use this project (**Python3**)

## Example of Use

Get the size of an struct executing: **?? sizeof(_PEB)** on Windbg:
```
?? sizeof(_PEB)
unsigned int 0x400
```

Execute **dt _PEB** on Windbg:
```
dt nt!_PEB
   +0x000 InheritedAddressSpace : UChar
   +0x001 ReadImageFileExecOptions : UChar
   +0x002 BeingDebugged    : UChar
   +0x003 BitField         : UChar
   +0x003 ImageUsesLargePages : Pos 0, 1 Bit
   +0x003 IsProtectedProcess : Pos 1, 1 Bit
   +0x003 IsImageDynamicallyRelocated : Pos 2, 1 Bit
   +0x003 SkipPatchingUser32Forwarders : Pos 3, 1 Bit
   +0x003 IsPackagedProcess : Pos 4, 1 Bit
   +0x003 IsAppContainer   : Pos 5, 1 Bit
   +0x003 IsProtectedProcessLight : Pos 6, 1 Bit
   +0x003 SpareBits        : Pos 7, 1 Bit
   +0x004 Padding0         : [4] UChar
   +0x008 Mutant           : Ptr64 Void
   +0x010 ImageBaseAddress : Ptr64 Void
   +0x018 Ldr              : Ptr64 _PEB_LDR_DATA
   +0x020 ProcessParameters : Ptr64 _RTL_USER_PROCESS_PARAMETERS
   +0x028 SubSystemData    : Ptr64 Void
   +0x030 ProcessHeap      : Ptr64 Void
   +0x038 FastPebLock      : Ptr64 _RTL_CRITICAL_SECTION
   +0x040 AtlThunkSListPtr : Ptr64 Void
   +0x048 IFEOKey          : Ptr64 Void
   +0x050 CrossProcessFlags : Uint4B
   +0x050 ProcessInJob     : Pos 0, 1 Bit
   +0x050 ProcessInitializing : Pos 1, 1 Bit
   +0x050 ProcessUsingVEH  : Pos 2, 1 Bit
   +0x050 ProcessUsingVCH  : Pos 3, 1 Bit
   +0x050 ProcessUsingFTH  : Pos 4, 1 Bit
   +0x050 ReservedBits0    : Pos 5, 27 Bits
   +0x054 Padding1         : [4] UChar
   +0x058 KernelCallbackTable : Ptr64 Void
   +0x058 UserSharedInfoPtr : Ptr64 Void
   +0x060 SystemReserved   : [1] Uint4B
   +0x064 AtlThunkSListPtr32 : Uint4B
   +0x068 ApiSetMap        : Ptr64 Void
   +0x070 TlsExpansionCounter : Uint4B
   +0x074 Padding2         : [4] UChar
   +0x078 TlsBitmap        : Ptr64 Void
   +0x080 TlsBitmapBits    : [2] Uint4B
   +0x088 ReadOnlySharedMemoryBase : Ptr64 Void
   +0x090 SparePvoid0      : Ptr64 Void
   +0x098 ReadOnlyStaticServerData : Ptr64 Ptr64 Void
   +0x0a0 AnsiCodePageData : Ptr64 Void
   +0x0a8 OemCodePageData  : Ptr64 Void
   +0x0b0 UnicodeCaseTableData : Ptr64 Void
   +0x0b8 NumberOfProcessors : Uint4B
   +0x0bc NtGlobalFlag     : Uint4B
   +0x0c0 CriticalSectionTimeout : _LARGE_INTEGER
   +0x0c8 HeapSegmentReserve : Uint8B
   +0x0d0 HeapSegmentCommit : Uint8B
   +0x0d8 HeapDeCommitTotalFreeThreshold : Uint8B
   +0x0e0 HeapDeCommitFreeBlockThreshold : Uint8B
   +0x0e8 NumberOfHeaps    : Uint4B
   +0x0ec MaximumNumberOfHeaps : Uint4B
   +0x0f0 ProcessHeaps     : Ptr64 Ptr64 Void
   +0x0f8 GdiSharedHandleTable : Ptr64 Void
   +0x100 ProcessStarterHelper : Ptr64 Void
   +0x108 GdiDCAttributeList : Uint4B
   +0x10c Padding3         : [4] UChar
   +0x110 LoaderLock       : Ptr64 _RTL_CRITICAL_SECTION
   +0x118 OSMajorVersion   : Uint4B
   +0x11c OSMinorVersion   : Uint4B
   +0x120 OSBuildNumber    : Uint2B
   +0x122 OSCSDVersion     : Uint2B
   +0x124 OSPlatformId     : Uint4B
   +0x128 ImageSubsystem   : Uint4B
   +0x12c ImageSubsystemMajorVersion : Uint4B
   +0x130 ImageSubsystemMinorVersion : Uint4B
   +0x134 Padding4         : [4] UChar
   +0x138 ActiveProcessAffinityMask : Uint8B
   +0x140 GdiHandleBuffer  : [60] Uint4B
   +0x230 PostProcessInitRoutine : Ptr64     void 
   +0x238 TlsExpansionBitmap : Ptr64 Void
   +0x240 TlsExpansionBitmapBits : [32] Uint4B
   +0x2c0 SessionId        : Uint4B
   +0x2c4 Padding5         : [4] UChar
   +0x2c8 AppCompatFlags   : _ULARGE_INTEGER
   +0x2d0 AppCompatFlagsUser : _ULARGE_INTEGER
   +0x2d8 pShimData        : Ptr64 Void
   +0x2e0 AppCompatInfo    : Ptr64 Void
   +0x2e8 CSDVersion       : _UNICODE_STRING
   +0x2f8 ActivationContextData : Ptr64 _ACTIVATION_CONTEXT_DATA
   +0x300 ProcessAssemblyStorageMap : Ptr64 _ASSEMBLY_STORAGE_MAP
   +0x308 SystemDefaultActivationContextData : Ptr64 _ACTIVATION_CONTEXT_DATA
   +0x310 SystemAssemblyStorageMap : Ptr64 _ASSEMBLY_STORAGE_MAP
   +0x318 MinimumStackCommit : Uint8B
   +0x320 FlsCallback      : Ptr64 _FLS_CALLBACK_INFO
   +0x328 FlsListHead      : _LIST_ENTRY
   +0x338 FlsBitmap        : Ptr64 Void
   +0x340 FlsBitmapBits    : [4] Uint4B
   +0x350 FlsHighIndex     : Uint4B
   +0x358 WerRegistrationData : Ptr64 Void
   +0x360 WerShipAssertPtr : Ptr64 Void
   +0x368 pUnused          : Ptr64 Void
   +0x370 pImageHeaderHash : Ptr64 Void
   +0x378 TracingFlags     : Uint4B
   +0x378 HeapTracingEnabled : Pos 0, 1 Bit
   +0x378 CritSecTracingEnabled : Pos 1, 1 Bit
   +0x378 LibLoaderTracingEnabled : Pos 2, 1 Bit
   +0x378 SpareTracingBits : Pos 3, 29 Bits
   +0x37c Padding6         : [4] UChar
   +0x380 CsrServerReadOnlySharedMemoryBase : Uint8B
   +0x388 TppWorkerpListLock : Uint8B
   +0x390 TppWorkerpList   : _LIST_ENTRY
```

Execute **python windbgtocstruct.py SIZE_OF_STRUCT**
```
python windbgtocstruct.py 0x400
```

Paste **Windbg dt output** and press enter two times

Done! this should be the C code generated: 
```
#include <Windows.h>
#pragma pack(push)
#pragma pack(1)

#define SIZEOF__PEB 0x400

typedef struct _PEB
{
        UCHAR InheritedAddressSpace; // 0x0
        UCHAR ReadImageFileExecOptions; // 0x1
        UCHAR BeingDebugged; // 0x2
        union aNoN_1
        {
                UCHAR BitField; // 0x3
                struct aNoN_2
                {
                        UCHAR ImageUsesLargePages : 1; // 0x3
                        UCHAR IsProtectedProcess : 1; // 0x3
                        UCHAR IsImageDynamicallyRelocated : 1; // 0x3
                        UCHAR SkipPatchingUser32Forwarders : 1; // 0x3
                        UCHAR IsPackagedProcess : 1; // 0x3
                        UCHAR IsAppContainer : 1; // 0x3
                        UCHAR IsProtectedProcessLight : 1; // 0x3
                        UCHAR SpareBits : 1; // 0x3
                } aNoN_3;
        } aNoN_4;
        UCHAR Padding0[4]; // 0x4
        PVOID Mutant; // 0x8
        PVOID ImageBaseAddress; // 0x10
        struct _PEB_LDR_DATA* Ldr; // 0x18
        struct _RTL_USER_PROCESS_PARAMETERS* ProcessParameters; // 0x20
        PVOID SubSystemData; // 0x28
        PVOID ProcessHeap; // 0x30
        struct _RTL_CRITICAL_SECTION* FastPebLock; // 0x38
        PVOID AtlThunkSListPtr; // 0x40
        PVOID IFEOKey; // 0x48
        union aNoN_6
        {
                ULONG CrossProcessFlags; // 0x50
                struct aNoN_7
                {
                        ULONG ProcessInJob : 1; // 0x50
                        ULONG ProcessInitializing : 1; // 0x50
                        ULONG ProcessUsingVEH : 1; // 0x50
                        ULONG ProcessUsingVCH : 1; // 0x50
                        ULONG ProcessUsingFTH : 1; // 0x50
                        ULONG ReservedBits0 : 27; // 0x50
                } aNoN_8;
        } aNoN_9;
        UCHAR Padding1[4]; // 0x54
        PVOID KernelCallbackTable; // 0x58
        PVOID UserSharedInfoPtr; // 0x58
        ULONG SystemReserved[1]; // 0x60
        ULONG AtlThunkSListPtr32; // 0x64
        PVOID ApiSetMap; // 0x68
        ULONG TlsExpansionCounter; // 0x70
        UCHAR Padding2[4]; // 0x74
        PVOID TlsBitmap; // 0x78
        ULONG TlsBitmapBits[2]; // 0x80
        PVOID ReadOnlySharedMemoryBase; // 0x88
        PVOID SparePvoid0; // 0x90
        PVOID* ReadOnlyStaticServerData; // 0x98
        PVOID AnsiCodePageData; // 0xA0
        PVOID OemCodePageData; // 0xA8
        PVOID UnicodeCaseTableData; // 0xB0
        ULONG NumberOfProcessors; // 0xB8
        ULONG NtGlobalFlag; // 0xBC
        struct _LARGE_INTEGER CriticalSectionTimeout; // 0xC0
        ULONG64 HeapSegmentReserve; // 0xC8
        ULONG64 HeapSegmentCommit; // 0xD0
        ULONG64 HeapDeCommitTotalFreeThreshold; // 0xD8
        ULONG64 HeapDeCommitFreeBlockThreshold; // 0xE0
        ULONG NumberOfHeaps; // 0xE8
        ULONG MaximumNumberOfHeaps; // 0xEC
        PVOID* ProcessHeaps; // 0xF0
        PVOID GdiSharedHandleTable; // 0xF8
        PVOID ProcessStarterHelper; // 0x100
        ULONG GdiDCAttributeList; // 0x108
        UCHAR Padding3[4]; // 0x10C
        struct _RTL_CRITICAL_SECTION* LoaderLock; // 0x110
        ULONG OSMajorVersion; // 0x118
        ULONG OSMinorVersion; // 0x11C
        USHORT OSBuildNumber; // 0x120
        USHORT OSCSDVersion; // 0x122
        ULONG OSPlatformId; // 0x124
        ULONG ImageSubsystem; // 0x128
        ULONG ImageSubsystemMajorVersion; // 0x12C
        ULONG ImageSubsystemMinorVersion; // 0x130
        UCHAR Padding4[4]; // 0x134
        ULONG64 ActiveProcessAffinityMask; // 0x138
        ULONG GdiHandleBuffer[60]; // 0x140
        void* PostProcessInitRoutine; // 0x230
        PVOID TlsExpansionBitmap; // 0x238
        ULONG TlsExpansionBitmapBits[32]; // 0x240
        ULONG SessionId; // 0x2C0
        UCHAR Padding5[4]; // 0x2C4
        struct _ULARGE_INTEGER AppCompatFlags; // 0x2C8
        struct _ULARGE_INTEGER AppCompatFlagsUser; // 0x2D0
        PVOID pShimData; // 0x2D8
        PVOID AppCompatInfo; // 0x2E0
        struct _UNICODE_STRING CSDVersion; // 0x2E8
        struct _ACTIVATION_CONTEXT_DATA* ActivationContextData; // 0x2F8
        struct _ASSEMBLY_STORAGE_MAP* ProcessAssemblyStorageMap; // 0x300
        struct _ACTIVATION_CONTEXT_DATA* SystemDefaultActivationContextData; // 0x308
        struct _ASSEMBLY_STORAGE_MAP* SystemAssemblyStorageMap; // 0x310
        ULONG64 MinimumStackCommit; // 0x318
        struct _FLS_CALLBACK_INFO* FlsCallback; // 0x320
        struct _LIST_ENTRY FlsListHead; // 0x328
        PVOID FlsBitmap; // 0x338
        ULONG FlsBitmapBits[4]; // 0x340
        ULONG FlsHighIndex; // 0x350
        PVOID WerRegistrationData; // 0x358
        PVOID WerShipAssertPtr; // 0x360
        PVOID pUnused; // 0x368
        PVOID pImageHeaderHash; // 0x370
        union aNoN_11
        {
                ULONG TracingFlags; // 0x378
                struct aNoN_12
                {
                        ULONG HeapTracingEnabled : 1; // 0x378
                        ULONG CritSecTracingEnabled : 1; // 0x378
                        ULONG LibLoaderTracingEnabled : 1; // 0x378
                        ULONG SpareTracingBits : 29; // 0x378
                } aNoN_13;
        } aNoN_14;
        UCHAR Padding6[4]; // 0x37C
        ULONG64 CsrServerReadOnlySharedMemoryBase; // 0x380
        ULONG64 TppWorkerpListLock; // 0x388
        struct _LIST_ENTRY TppWorkerpList; // 0x390
} PEB, *PPEB;

// Dummy structs:
struct _PEB_LDR_DATA
{
        UCHAR data[1];
};

struct _RTL_USER_PROCESS_PARAMETERS
{
        UCHAR data[1];
};

struct _RTL_CRITICAL_SECTION
{
        UCHAR data[1];
};

struct _LARGE_INTEGER
{
        UCHAR data[8];
};

struct _ULARGE_INTEGER
{
        UCHAR data[8];
};

struct _UNICODE_STRING
{
        UCHAR data[16];
};

struct _ACTIVATION_CONTEXT_DATA
{
        UCHAR data[1];
};

struct _ASSEMBLY_STORAGE_MAP
{
        UCHAR data[1];
};

struct _FLS_CALLBACK_INFO
{
        UCHAR data[1];
};

struct _LIST_ENTRY
{
        UCHAR data[16];
};


#pragma pack(pop)
```

Copy C code to your project and remove already defined dummy structs.

**WARNING:** Dont use sizeof(STRUCT), because the last member of the struct can be non-completed. Use **SIZEOF__PEB** generated by the script

Example:
```
PPEB peb_ptr = malloc(SIZEOF__PEB);
....
ExternalApiUsingPEB(arg1, arg2, ..., SIZEOF__PEB, peb_ptr, ...);
```

## TODO

* Still not able to properly handle nested unions and structs.

## Related

* https://github.com/ajkhoury/Windbg2Struct

* https://github.com/markhc/windbg_to_c