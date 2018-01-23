#!/usr/bin/python3
# encoding: utf8

import os
import sys


SDK_ROOT = "/home/solomon/workspace/bluetooth/nRF5_SDK_14.2.0_17b948a"
DEVICE = "NRF52"
DEVICE_VARIANT = "xxaa"
BOARD = "BOARD_PCA10036"
SXXX = "s132"
SDK_CONFIG_FILE = "./config/sdk_config.h"

MAKEFILE_INC = "_makefile"
DEVICE_LC = DEVICE.lower()
OUTPUT_DIRECTORY = "_build"
TEMPLATE_PATH = f"{SDK_ROOT}/components/toolchain/gcc"
TARGETS = f"{DEVICE_LC}_{DEVICE_VARIANT}"

LINKER_SCRIPT = f"{SDK_ROOT}/components/toolchain/gcc/{DEVICE_LC}_{DEVICE_VARIANT}.ld"

SRC_FILES = set([
    "src/main.c",
    "src/led.c",

    f"{SDK_ROOT}/components/boards/boards.c",
    f"{SDK_ROOT}/components/toolchain/system_{DEVICE_LC}.c",
    f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_{DEVICE_LC}.S",

    f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",
])

INC_FOLDERS = set([
    f"{SDK_ROOT}/components/softdevice/{SXXX}/headers",
    f"{SDK_ROOT}/components/device",
    f"{SDK_ROOT}/components/boards",
    f"{SDK_ROOT}/components/drivers_nrf/nrf_soc_nosd",
    f"{SDK_ROOT}/components/libraries/util",
    f"{SDK_ROOT}/components/drivers_nrf/hal",
    f"{SDK_ROOT}/components/drivers_nrf/delay",
    f"{SDK_ROOT}/components/toolchain",
    f"{SDK_ROOT}/components/toolchain/gcc",
    f"{SDK_ROOT}/components/toolchain/cmsis/include",
    f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers",
])

MACRO = set([
    f"{DEVICE}",
    f"{BOARD}",
])

CFLAGS = set([
    "-Wall",
    # "-Werror",

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
])

LDFLAGS = set([
    "-mthumb",
    "-mabi=aapcs",
    f"-L{TEMPLATE_PATH}",
    "-mcpu=cortex-m4",

    # let linker dump unused sections
    "-Wl,--gc-sections",

    # use newlib in nano version
    "--specs=nano.specs",
])

LIB_FILES = set([
    "-lc",
    "-lnosys",
    "-lm",
])


def generate_makefile():
    if not os.path.exists(MAKEFILE_INC):
        os.mkdir(MAKEFILE_INC)

    with open(f"{MAKEFILE_INC}/Makefile.common", "w") as fd:
        fd.writelines([
            f"DEVICE = {DEVICE}\n",
            f"DEVICE_VARIANT = {DEVICE_VARIANT}\n",
            f"DEVICE_LC = {DEVICE_LC}\n",

            f"BOARD = {BOARD}\n",

            f"SDK_ROOT = {SDK_ROOT}\n",
            f"TARGETS = {TARGETS}\n",
            f"OUTPUT_DIRECTORY = {OUTPUT_DIRECTORY}\n",
            f"TEMPLATE_PATH = {TEMPLATE_PATH}\n",

            f"LINKER_SCRIPT = {LINKER_SCRIPT}\n",

            f"SDK_CONFIG_FILE := {SDK_CONFIG_FILE}\n",
        ])

    with open(f"{MAKEFILE_INC}/Makefile.src", "w") as fd:
        fd.writelines([f"SRC_FILES += {x}\n" for x in SRC_FILES])

    with open(f"{MAKEFILE_INC}/Makefile.inc", "w") as fd:
        INC_FOLDERS.add(os.path.dirname(SDK_CONFIG_FILE))
        fd.writelines([f"INC_FOLDERS += {x}\n" for x in INC_FOLDERS])

    with open(f"{MAKEFILE_INC}/Makefile.flags", "w") as fd:
        fd.writelines([f"CFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"CFLAGS += -D{x}\n" for x in MACRO])

        fd.writelines([f"ASMFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"ASMFLAGS += -D{x}\n" for x in MACRO])

        LDFLAGS.add(f"-T{LINKER_SCRIPT}")
        fd.writelines([f"LDFLAGS += {x}\n" for x in LDFLAGS])

    with open(f"{MAKEFILE_INC}/Makefile.lib", "w") as fd:
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


def __set_remove(s: set, e):
    if e in s:
        s.remove(e)


def set_debug(debug: bool):
    if debug:
        __set_remove(CFLAGS, "-O3")
        MACRO.add("DEBUG")
        CFLAGS.add("-O -ggdb")
    else:
        CFLAGS.add("-O3")
        __set_remove(MACRO, "DEBUG")
        __set_remove(CFLAGS, "-O -ggdb")
