#!/usr/bin/python3
# encoding: utf8

import os
import sys


SDK_ROOT = "/home/solomon/workspace/bluetooth/nRF5_SDK_14.2.0_17b948a"
# SDK_ROOT = "/home/solomon/workspace/bluetooth/nRF5_SDK_14.0.0_3bcc1f7"
DEVICE = "NRF52"
DEVICE_VARIANT = "xxaa"
BOARD = "BOARD_PCA10040"
SXXX = "s132"
SDK_CONFIG_FILE = "./config/sdk_config.h"
# SOFTDEVICE = f"{SDK_ROOT}/components/softdevice/s112/hex/s112_nrf52810_5.1.0_softdevice.hex"
SOFTDEVICE = f"{SDK_ROOT}/components/softdevice/s132/hex/s132_nrf52_5.0.0_softdevice.hex"

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

		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_rtt.c",
		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_serial.c",
		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_uart.c",
		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_default_backends.c",
		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_frontend.c",
		f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_str_formatter.c",
		f"{SDK_ROOT}/components/libraries/button/app_button.c",
		f"{SDK_ROOT}/components/libraries/util/app_error.c",
		f"{SDK_ROOT}/components/libraries/util/app_error_weak.c",
		f"{SDK_ROOT}/components/libraries/scheduler/app_scheduler.c",
		f"{SDK_ROOT}/components/libraries/timer/app_timer.c",
		f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",
		f"{SDK_ROOT}/components/libraries/crc16/crc16.c",
		f"{SDK_ROOT}/components/libraries/fds/fds.c",
		f"{SDK_ROOT}/components/libraries/hardfault/hardfault_implementation.c",
		f"{SDK_ROOT}/components/libraries/util/nrf_assert.c",
		f"{SDK_ROOT}/components/libraries/atomic_fifo/nrf_atfifo.c",
		f"{SDK_ROOT}/components/libraries/balloc/nrf_balloc.c",
		f"{SDK_ROOT}/external/fprintf/nrf_fprintf.c",
		f"{SDK_ROOT}/external/fprintf/nrf_fprintf_format.c",
		f"{SDK_ROOT}/components/libraries/fstorage/nrf_fstorage.c",
		f"{SDK_ROOT}/components/libraries/fstorage/nrf_fstorage_sd.c",
		f"{SDK_ROOT}/components/libraries/experimental_memobj/nrf_memobj.c",
		f"{SDK_ROOT}/components/libraries/pwr_mgmt/nrf_pwr_mgmt.c",
		f"{SDK_ROOT}/components/libraries/experimental_section_vars/nrf_section_iter.c",
		f"{SDK_ROOT}/components/libraries/strerror/nrf_strerror.c",
		f"{SDK_ROOT}/components/libraries/util/sdk_mapped_flags.c",
		f"{SDK_ROOT}/components/libraries/sensorsim/sensorsim.c",
		f"{SDK_ROOT}/components/boards/boards.c",
		f"{SDK_ROOT}/components/drivers_nrf/clock/nrf_drv_clock.c",
		f"{SDK_ROOT}/components/drivers_nrf/common/nrf_drv_common.c",
		f"{SDK_ROOT}/components/drivers_nrf/gpiote/nrf_drv_gpiote.c",
		f"{SDK_ROOT}/components/drivers_nrf/uart/nrf_drv_uart.c",
		f"{SDK_ROOT}/components/libraries/bsp/bsp.c",
		f"{SDK_ROOT}/components/libraries/bsp/bsp_btn_ble.c",
		f"{SDK_ROOT}/components/libraries/bsp/bsp_nfc.c",
		f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
		f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",
		f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
		f"{SDK_ROOT}/components/ble/common/ble_advdata.c",
		f"{SDK_ROOT}/components/ble/ble_advertising/ble_advertising.c",
		f"{SDK_ROOT}/components/ble/common/ble_conn_params.c",
		f"{SDK_ROOT}/components/ble/common/ble_conn_state.c",
		f"{SDK_ROOT}/components/ble/common/ble_srv_common.c",
		f"{SDK_ROOT}/components/ble/peer_manager/gatt_cache_manager.c",
		f"{SDK_ROOT}/components/ble/peer_manager/gatts_cache_manager.c",
		f"{SDK_ROOT}/components/ble/peer_manager/id_manager.c",
		f"{SDK_ROOT}/components/ble/nrf_ble_gatt/nrf_ble_gatt.c",
		f"{SDK_ROOT}/components/ble/peer_manager/peer_data_storage.c",
		f"{SDK_ROOT}/components/ble/peer_manager/peer_database.c",
		f"{SDK_ROOT}/components/ble/peer_manager/peer_id.c",
		f"{SDK_ROOT}/components/ble/peer_manager/peer_manager.c",
		f"{SDK_ROOT}/components/ble/peer_manager/pm_buffer.c",
		f"{SDK_ROOT}/components/ble/peer_manager/pm_mutex.c",
		f"{SDK_ROOT}/components/ble/peer_manager/security_dispatcher.c",
		f"{SDK_ROOT}/components/ble/peer_manager/security_manager.c",
		f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_nrf52.S",
		f"{SDK_ROOT}/components/toolchain/system_nrf52.c",
		f"{SDK_ROOT}/components/softdevice/common/nrf_sdh.c",
		f"{SDK_ROOT}/components/softdevice/common/nrf_sdh_ble.c",
		f"{SDK_ROOT}/components/softdevice/common/nrf_sdh_soc.c",
    ]
    __list_append(SRC_FILES, l)


def __add_base_inc():
    l = [
        "src",
		f"{SDK_ROOT}/components/drivers_nrf/comp",
		f"{SDK_ROOT}/components/drivers_nrf/twi_master",
		f"{SDK_ROOT}/components/ble/ble_services/ble_ancs_c",
		f"{SDK_ROOT}/components/ble/ble_services/ble_ias_c",
		f"{SDK_ROOT}/components/libraries/pwm",
		f"{SDK_ROOT}/components/softdevice/s132/headers/nrf52",
		f"{SDK_ROOT}/components/libraries/usbd/class/cdc/acm",
		f"{SDK_ROOT}/components/libraries/usbd/class/hid/generic",
		f"{SDK_ROOT}/components/libraries/usbd/class/msc",
		f"{SDK_ROOT}/components/libraries/usbd/class/hid",
		f"{SDK_ROOT}/components/libraries/experimental_log",
		f"{SDK_ROOT}/components/ble/ble_services/ble_gls",
		f"{SDK_ROOT}/components/libraries/fstorage",
		f"{SDK_ROOT}/components/drivers_nrf/i2s",
		f"{SDK_ROOT}/components/libraries/mutex",
		f"{SDK_ROOT}/components/libraries/gpiote",
		f"{SDK_ROOT}/components/libraries/experimental_log/src",
		f"{SDK_ROOT}/components/drivers_nrf/gpiote",
		f"{SDK_ROOT}/components/boards",
		f"{SDK_ROOT}/components/libraries/experimental_memobj",
		f"{SDK_ROOT}/components/drivers_nrf/common",
		f"{SDK_ROOT}/components/ble/ble_advertising",
		f"{SDK_ROOT}/components/ble/ble_services/ble_bas_c",
		f"{SDK_ROOT}/components/ble/ble_services/ble_hrs_c",
		f"{SDK_ROOT}/components/libraries/queue",
		f"{SDK_ROOT}/components/libraries/pwr_mgmt",
		f"{SDK_ROOT}/components/ble/ble_dtm",
		f"{SDK_ROOT}/components/toolchain/cmsis/include",
		f"{SDK_ROOT}/components/ble/ble_services/ble_rscs_c",
		f"{SDK_ROOT}/components/drivers_nrf/uart",
		f"{SDK_ROOT}/components/ble/common",
		f"{SDK_ROOT}/components/ble/ble_services/ble_lls",
		f"{SDK_ROOT}/components/drivers_nrf/wdt",
		f"{SDK_ROOT}/components/libraries/bsp",
		f"{SDK_ROOT}/components/ble/ble_services/ble_bas",
		f"{SDK_ROOT}/components/libraries/experimental_section_vars",
		f"{SDK_ROOT}/components/softdevice/s132/headers",
		f"{SDK_ROOT}/components/ble/ble_services/ble_ans_c",
		f"{SDK_ROOT}/components/libraries/slip",
		f"{SDK_ROOT}/components/libraries/mem_manager",
		f"{SDK_ROOT}/external/segger_rtt",
		f"{SDK_ROOT}/components/libraries/usbd/class/cdc",
		f"{SDK_ROOT}/components/drivers_nrf/hal",
		f"{SDK_ROOT}/components/ble/ble_services/ble_nus_c",
		f"{SDK_ROOT}/components/drivers_nrf/rtc",
		f"{SDK_ROOT}/components/softdevice/common",
		f"{SDK_ROOT}/components/ble/ble_services/ble_ias",
		f"{SDK_ROOT}/components/libraries/usbd/class/hid/mouse",
		f"{SDK_ROOT}/components/libraries/ecc",
		f"{SDK_ROOT}/components/drivers_nrf/ppi",
		f"{SDK_ROOT}/components/ble/ble_services/ble_dfu",
		f"{SDK_ROOT}/external/fprintf",
		f"{SDK_ROOT}/components/drivers_nrf/twis_slave",
		f"{SDK_ROOT}/components/libraries/atomic",
		f"{SDK_ROOT}/components",
		f"{SDK_ROOT}/components/libraries/scheduler",
		f"{SDK_ROOT}/components/libraries/cli",
		f"{SDK_ROOT}/components/ble/ble_services/ble_lbs",
		f"{SDK_ROOT}/components/ble/ble_services/ble_hts",
		f"{SDK_ROOT}/components/drivers_nrf/delay",
		f"{SDK_ROOT}/components/libraries/crc16",
		f"{SDK_ROOT}/components/drivers_nrf/timer",
		f"{SDK_ROOT}/components/libraries/util",
		f"{SDK_ROOT}/components/drivers_nrf/pwm",
		f"{SDK_ROOT}/components/libraries/csense_drv",
		f"{SDK_ROOT}/components/libraries/csense",
		f"{SDK_ROOT}/components/libraries/balloc",
		f"{SDK_ROOT}/components/libraries/low_power_pwm",
		f"{SDK_ROOT}/components/libraries/hardfault",
		f"{SDK_ROOT}/components/ble/ble_services/ble_cscs",
		f"{SDK_ROOT}/components/libraries/uart",
		f"{SDK_ROOT}/components/libraries/hci",
		f"{SDK_ROOT}/components/libraries/usbd/class/hid/kbd",
		f"{SDK_ROOT}/components/drivers_nrf/spi_slave",
		f"{SDK_ROOT}/components/drivers_nrf/lpcomp",
		f"{SDK_ROOT}/components/libraries/timer",
		f"{SDK_ROOT}/components/drivers_nrf/rng",
		f"{SDK_ROOT}/components/drivers_nrf/power",
		f"{SDK_ROOT}/components/libraries/usbd/config",
		f"{SDK_ROOT}/components/toolchain",
		f"{SDK_ROOT}/components/libraries/led_softblink",
		f"{SDK_ROOT}/components/drivers_nrf/qdec",
		f"{SDK_ROOT}/components/ble/ble_services/ble_cts_c",
		f"{SDK_ROOT}/components/drivers_nrf/spi_master",
		f"{SDK_ROOT}/components/ble/ble_services/ble_nus",
		f"{SDK_ROOT}/components/libraries/twi_mngr",
		f"{SDK_ROOT}/components/ble/ble_services/ble_hids",
		f"{SDK_ROOT}/components/libraries/strerror",
		f"{SDK_ROOT}/components/drivers_nrf/pdm",
		f"{SDK_ROOT}/components/libraries/crc32",
		f"{SDK_ROOT}/components/libraries/usbd/class/audio",
		f"{SDK_ROOT}/components/libraries/sensorsim",
		f"{SDK_ROOT}/components/ble/peer_manager",
		f"{SDK_ROOT}/components/drivers_nrf/swi",
		f"{SDK_ROOT}/components/ble/ble_services/ble_tps",
		f"{SDK_ROOT}/components/ble/ble_services/ble_dis",
		f"{SDK_ROOT}/components/device",
		f"{SDK_ROOT}/components/ble/nrf_ble_gatt",
		f"{SDK_ROOT}/components/ble/nrf_ble_qwr",
		f"{SDK_ROOT}/components/libraries/button",
		f"{SDK_ROOT}/components/libraries/usbd",
		f"{SDK_ROOT}/components/drivers_nrf/saadc",
		f"{SDK_ROOT}/components/libraries/atomic_fifo",
		f"{SDK_ROOT}/components/ble/ble_services/ble_lbs_c",
		f"{SDK_ROOT}/components/ble/ble_racp",
		f"{SDK_ROOT}/components/toolchain/gcc",
		f"{SDK_ROOT}/components/libraries/fds",
		f"{SDK_ROOT}/components/libraries/twi",
		f"{SDK_ROOT}/components/drivers_nrf/clock",
		f"{SDK_ROOT}/components/ble/ble_services/ble_rscs",
		f"{SDK_ROOT}/components/drivers_nrf/usbd",
		f"{SDK_ROOT}/components/ble/ble_services/ble_hrs",
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
        "CONFIG_GPIO_AS_PINRESET",
        "FLOAT_ABI_HARD",
        "SOFTDEVICE_PRESENT",
        "SWI_DISABLE0",
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
