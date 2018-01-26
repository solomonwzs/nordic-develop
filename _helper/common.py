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
SOFTDEVICE = f"{SDK_ROOT}/components/softdevice/s112/hex/s112_nrf52810_5.1.0_softdevice.hex"

MAKEFILE_INC = "_makefile"
DEVICE_LC = DEVICE.lower()
OUTPUT_DIRECTORY = "_build"
TEMPLATE_PATH = f"{SDK_ROOT}/components/toolchain/gcc"
TARGETS = f"{DEVICE_LC}_{DEVICE_VARIANT}"

# LINKER_SCRIPT = f"{SDK_ROOT}/components/toolchain/gcc/{DEVICE_LC}_{DEVICE_VARIANT}.ld"
LINKER_SCRIPT = "./ld/nrf.ld"

SRC_FILES = []
INC_FOLDERS = []
MACRO = []
CFLAGS = []
LDFLAGS = []
LIB_FILES = []


def __add_base_src():
    l = [
        "src/main.c",
        "src/my_init.c",

        f"{SDK_ROOT}/components/toolchain/system_{DEVICE_LC}.c",
        f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_{DEVICE_LC}.S",

        f"{SDK_ROOT}/components/ble/ble_services/ble_cts_c/ble_cts_c.c",
        f"{SDK_ROOT}/components/libraries/bsp/bsp.c",
        f"{SDK_ROOT}/components/libraries/timer/app_timer.c",
        f"{SDK_ROOT}/components/libraries/scheduler/app_scheduler.c",
        f"{SDK_ROOT}/components/libraries/scheduler/app_scheduler.c",
        f"{SDK_ROOT}/components/libraries/experimental_section_vars/nrf_section_iter.c",
        f"{SDK_ROOT}/components/libraries/util/sdk_mapped_flags.c",
        f"{SDK_ROOT}/components/libraries/fds/fds.c",
        f"{SDK_ROOT}/components/libraries/fstorage/nrf_fstorage.c",
        f"{SDK_ROOT}/components/libraries/atomic_fifo/nrf_atfifo.c",

        f"{SDK_ROOT}/components/ble/peer_manager/peer_manager.c",
        f"{SDK_ROOT}/components/ble/peer_manager/peer_id.c",
        f"{SDK_ROOT}/components/ble/peer_manager/security_manager.c",
        f"{SDK_ROOT}/components/ble/peer_manager/security_dispatcher.c",
        f"{SDK_ROOT}/components/ble/peer_manager/id_manager.c",
        f"{SDK_ROOT}/components/ble/peer_manager/peer_database.c",
        f"{SDK_ROOT}/components/ble/peer_manager/pm_buffer.c",
        f"{SDK_ROOT}/components/ble/peer_manager/pm_mutex.c",
        f"{SDK_ROOT}/components/ble/peer_manager/gatts_cache_manager.c",
        f"{SDK_ROOT}/components/ble/peer_manager/gatt_cache_manager.c",
        f"{SDK_ROOT}/components/ble/peer_manager/peer_data_storage.c",

        f"{SDK_ROOT}/components/softdevice/common/nrf_sdh.c",
        f"{SDK_ROOT}/components/softdevice/common/nrf_sdh_ble.c",

        f"{SDK_ROOT}/components/ble/common/ble_conn_state.c",
    ]
    __list_append(SRC_FILES, l)


def __add_base_inc():
    l = [
        "src",

        f"{SDK_ROOT}/components/libraries/bsp",
        f"{SDK_ROOT}/components/libraries/button",

        f"{SDK_ROOT}/components/libraries/timer",

        f"{SDK_ROOT}/components/ble/peer_manager",
        f"{SDK_ROOT}/components/ble/common",
        f"{SDK_ROOT}/components/ble/ble_services/ble_cts_c",
        f"{SDK_ROOT}/components/ble/ble_db_discovery",

        f"{SDK_ROOT}/components/libraries/scheduler",
        f"{SDK_ROOT}/components/libraries/fds",
        f"{SDK_ROOT}/components/libraries/atomic_fifo",
        f"{SDK_ROOT}/components/libraries/fstorage",

        f"{SDK_ROOT}/components/softdevice/common",
    ]
    __list_append(INC_FOLDERS, l)


def __add_base_macro():
    l = [
        DEVICE,
        BOARD,
        "NRF_LOG_ENABLED",
        "NRF52832_XXAA",
        SXXX.upper(),
        "NRF_SD_BLE_API_VERSION=5",
    ]
    __list_append(MACRO, l)


def __add_base_flags():
    l = [
        "-Wall",
        # "-Werror",

        "-mcpu=cortex-m4",
        "-mthumb",
        "-mabi=aapcs",

        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard",

        "-ffunction-sections",
        "-fdata-sections",
        "-fno-strict-aliasing",
        "-fno-builtin",
        "-fshort-enums",
    ]
    __list_append(CFLAGS, l)


def __add_base_ldflags():
    l = [
        "-mthumb",
        "-mabi=aapcs",
        f"-L{TEMPLATE_PATH}",
        "-mcpu=cortex-m4",

        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard",

        # let linker dump unused sections
        "-Wl,--gc-sections",

        # use newlib in nano version
        "--specs=nano.specs",
    ]
    __list_append(LDFLAGS, l)


def __add_base_libs():
    l = [
        "-lc",
        "-lnosys",
        "-lm",
    ]
    __list_append(LIB_FILES, l)


def __ad_base():
    __add_base_src()
    __add_base_inc()
    __add_base_macro()
    __add_base_flags()
    __add_base_ldflags()
    __add_base_libs()


def generate_makefile():
    if not os.path.exists(MAKEFILE_INC):
        os.mkdir(MAKEFILE_INC)

    __ad_base()
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
            f"SOFTDEVICE := {SOFTDEVICE}\n",
        ])

    with open(f"{MAKEFILE_INC}/Makefile.src", "w") as fd:
        fd.writelines([f"SRC_FILES += {x}\n" for x in SRC_FILES])

    with open(f"{MAKEFILE_INC}/Makefile.inc", "w") as fd:
        INC_FOLDERS.append(os.path.dirname(SDK_CONFIG_FILE))
        fd.writelines([f"INC_FOLDERS += {x}\n" for x in INC_FOLDERS])

    with open(f"{MAKEFILE_INC}/Makefile.flags", "w") as fd:
        fd.writelines([f"CFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"CFLAGS += -D{x}\n" for x in MACRO])

        fd.writelines([f"ASMFLAGS += {x}\n" for x in CFLAGS])
        fd.writelines([f"ASMFLAGS += -D{x}\n" for x in MACRO])

        LDFLAGS.append(f"-T{LINKER_SCRIPT}")
        fd.writelines([f"LDFLAGS += {x}\n" for x in LDFLAGS])

    with open(f"{MAKEFILE_INC}/Makefile.lib", "w") as fd:
        fd.writelines([f"LIB_FILES += {x}\n" for x in LIB_FILES])


def generate_vim_syntastic():
    __ad_base()
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


def __list_remove(s: list, e):
    if e in s:
        s.remove(e)


def __list_append(ori: list, n: list):
    for e in ori:
        if e in n:
            n.remove(e)
    ori.extend(n)


def list_union(ori: list, n: list):
    for e in n:
        if e in ori:
            ori.remove(e)
    ori.reverse()
    n.reverse()
    ori.extend(n)
    ori.reverse()


def set_debug(debug: bool):
    if debug:
        __list_remove(CFLAGS, "-O3")
        MACRO.append("DEBUG")
        CFLAGS.append("-O -ggdb")
    else:
        CFLAGS.append("-O3")
        __list_remove(MACRO, "DEBUG")
        __list_remove(CFLAGS, "-O -ggdb")
