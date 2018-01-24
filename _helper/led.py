#!/usr/bin/python3
# encoding: utf8

from common import (
    SXXX,
    SDK_ROOT,
    list_union,
    DEVICE_LC,
)
import common


__SRC = [
    "src/led.c",

    f"{SDK_ROOT}/components/boards/boards.c",
    f"{SDK_ROOT}/components/toolchain/system_{DEVICE_LC}.c",
    f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_{DEVICE_LC}.S",

    f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",

    f"{SDK_ROOT}/components/libraries/util/app_error.c",
    f"{SDK_ROOT}/components/libraries/util/app_error_weak.c",
]

__INC = [
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
]

def add_led_support():
    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
