#!/usr/bin/python3
# encoding: utf8

from common import (
    SXXX,
    SDK_ROOT,
    list_union,
    DEVICE_LC,
)
import common


def add_led_support():
    __SRC = [
        "src/my_led.c",

        f"{SDK_ROOT}/components/boards/boards.c",

    ]
    __INC = [
        f"{SDK_ROOT}/components/softdevice/{SXXX}/headers",
        f"{SDK_ROOT}/components/device",
        f"{SDK_ROOT}/components/boards",
        f"{SDK_ROOT}/components/libraries/util",
        f"{SDK_ROOT}/components/drivers_nrf/hal",
        f"{SDK_ROOT}/components/drivers_nrf/delay",
        f"{SDK_ROOT}/components/toolchain",
        f"{SDK_ROOT}/components/toolchain/cmsis/include",
    ]

    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
