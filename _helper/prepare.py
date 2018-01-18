#!/usr/bin/python3
# encoding: utf8

import os
import sys


SDK_ROOT = "/home/solomon/workspace/bluetooth/nRF5_SDK_14.2.0_17b948a"
DEVICE = "NRF52"
DEVICE_VARIANT = "xxaa"
BOARD = "BOARD_PCA10036"

__MAKEFILE_INC = "_makefile"
__DEVICE_LC = DEVICE.lower()
__OUTPUT_DIRECTORY = "_build"
__TEMPLATE_PATH = f"{SDK_ROOT}/components/toolchain/gcc"
__TARGETS = f"{__DEVICE_LC}_{DEVICE_VARIANT}"

LINKER_SCRIPT = f"{SDK_ROOT}/components/toolchain/gcc/{__DEVICE_LC}_{DEVICE_VARIANT}.ld"

SRC_FILES = [
    "src/main.c",
    "src/led.c",
    f"{SDK_ROOT}/components/boards/boards.c",
    f"{SDK_ROOT}/components/toolchain/system_{__DEVICE_LC}.c",
    f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_{__DEVICE_LC}.S",

    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",

    f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",
]

INC_FOLDERS = [
    f"{SDK_ROOT}/config",
    f"{SDK_ROOT}/components/softdevice/s140/headers",
    f"{SDK_ROOT}/components/device",
    f"{SDK_ROOT}/components/boards",
    f"{SDK_ROOT}/components/drivers_nrf/nrf_soc_nosd",
    f"{SDK_ROOT}/components/libraries/util",
    f"{SDK_ROOT}/components/drivers_nrf/hal",
    f"{SDK_ROOT}/components/drivers_nrf/delay",
    f"{SDK_ROOT}/components/toolchain",
    f"{SDK_ROOT}/components/toolchain/gcc",
    f"{SDK_ROOT}/components/toolchain/cmsis/include",
    f"{SDK_ROOT}/external/segger_rtt",
]

MACRO = [
    f"{DEVICE}",
    f"{BOARD}",
]

CFLAGS = [
    "-O -ggdb",
    "-Wall",
    "-Werror",

    "-mcpu=cortex-m4",
    "-mthumb",
    "-mabi=aapcs",
    "-mfpu=fpv4-sp-d16",
    "-mfloat-abi=soft",

    "-ffunction-sections",
    "-fdata-sections",
    "-fno-strict-aliasing",
    "-fno-builtin",
    "-fshort-enums",
]

LDFLAGS = [
    "-mthumb",
    "-mabi=aapcs",
    f"-L{__TEMPLATE_PATH}",
    f"-T{LINKER_SCRIPT}",
    "-mcpu=cortex-m4",

    # let linker dump unused sections
    "-Wl,--gc-sections",

    # use newlib in nano version
    "--specs=nano.specs",
]

LIB_FILES = [
    "-lc",
    "-lnosys",
    "-lm",
]


def generate_makefile():
    if not os.path.exists(__MAKEFILE_INC):
        os.mkdir(__MAKEFILE_INC)

    with open(f"{__MAKEFILE_INC}/Makefile.common", "w") as fd:
        fd.writelines([
            f"DEVICE = {DEVICE}\n",
            f"DEVICE_VARIANT = {DEVICE_VARIANT}\n",
            f"DEVICE_LC = {__DEVICE_LC}\n",

            f"BOARD = {BOARD}\n",

            f"SDK_ROOT = {SDK_ROOT}\n",
            f"TARGETS = {__TARGETS}\n",
            f"OUTPUT_DIRECTORY = {__OUTPUT_DIRECTORY}\n",
            f"TEMPLATE_PATH = {__TEMPLATE_PATH}\n",

            f"LINKER_SCRIPT = {LINKER_SCRIPT}\n",
        ])

    with open(f"{__MAKEFILE_INC}/Makefile.src", "w") as fd:
        fd.writelines([f"SRC_FILES += {x}\n" for x in SRC_FILES])

    with open(f"{__MAKEFILE_INC}/Makefile.inc", "w") as fd:
        fd.writelines([f"INC_FOLDERS += {x}\n" for x in INC_FOLDERS])

    with open(f"{__MAKEFILE_INC}/Makefile.flags", "w") as fd:
        fd.writelines([f"CFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"CFLAGS += -D{x}\n" for x in MACRO])

        fd.writelines([f"ASMFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"ASMFLAGS += -D{x}\n" for x in MACRO])

        fd.writelines([f"LDFLAGS += {x}\n" for x in LDFLAGS])

    with open(f"{__MAKEFILE_INC}/Makefile.lib", "w") as fd:
        fd.writelines([f"LIB_FILES += {x}\n" for x in LIB_FILES])


def generate_vim_syntastic():
    with open("my.vim", "w") as fd:
        fd.write("let g:syntastic_c_compiler = 'arm-none-eabi-gcc'\n")

        inc = ",".join([f"'{x}'" for x in INC_FOLDERS])
        fd.write(f"let g:syntastic_c_include_dirs = [{inc}]\n")

        macro = " ".join([f"-D{x}" for x in MACRO])
        fd.write(f"let g:syntastic_c_compiler_options = '{macro}'\n")


def generate_cscope():
    cscope_files = ".cscope.files"
    os.system(f"find . -iname '*.c' -o -iname '*.cpp' -o -iname '*.h' " +
              f"-o -iname '*.hpp' -o -iname '*.cc' > {cscope_files}")
    os.system(f"find {SDK_ROOT} -iname '*.c' -o -iname '*.cpp' " +
              f"-o -iname '*.h' -o -iname '*.hpp' -o -iname '*.cc' " +
              f">> {cscope_files}")
    os.system(f"cscope -bq -i {cscope_files} -f cscope.out")
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "makefile":
            generate_makefile()
        elif sys.argv[1] == "vim":
            generate_vim_syntastic()
        elif sys.argv[1] == "cscope":
            generate_cscope()
    else:
        generate_makefile()
        generate_vim_syntastic()
        generate_cscope()
