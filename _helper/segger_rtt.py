#!/usr/bin/python3
# encoding: utf8

import common
from common import (
    SDK_ROOT,
    list_union,
    SXXX,
)


def add_rtt_support():
    __SRC = [
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",

        f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",
    ]

    __INC = [
        f"{SDK_ROOT}/external/segger_rtt",

        f"{SDK_ROOT}/components/softdevice/{SXXX}/headers",
        f"{SDK_ROOT}/components/device",
        f"{SDK_ROOT}/components/libraries/util",
        f"{SDK_ROOT}/components/drivers_nrf/delay",
        f"{SDK_ROOT}/components/toolchain",
        f"{SDK_ROOT}/components/toolchain/cmsis/include",
    ]
    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
