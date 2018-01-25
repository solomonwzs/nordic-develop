#!/usr/bin/python3
# encoding: utf8

from common import (
    SXXX,
    SDK_ROOT,
    list_union,
    DEVICE_LC,
)
import common


def add_log_support():
    __SRC = [
        f"{SDK_ROOT}/components/libraries/util/app_error.c",
        f"{SDK_ROOT}/components/libraries/util/app_error_weak.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_frontend.c",

        f"{SDK_ROOT}/components/libraries/balloc/nrf_balloc.c",
        f"{SDK_ROOT}/components/libraries/experimental_memobj/nrf_memobj.c",

        f"{SDK_ROOT}/components/libraries/strerror/nrf_strerror.c",
        f"{SDK_ROOT}/components/libraries/cli/nrf_cli.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_default_backends.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_rtt.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_serial.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_str_formatter.c",

        f"{SDK_ROOT}/external/fprintf/nrf_fprintf.c",
        f"{SDK_ROOT}/external/fprintf/nrf_fprintf_format.c",
    ]
    __INC = [
        f"{SDK_ROOT}/components/libraries/atomic",
        f"{SDK_ROOT}/components/libraries/balloc",
        f"{SDK_ROOT}/components/libraries/cli",
        f"{SDK_ROOT}/components/libraries/queue",
        f"{SDK_ROOT}/components/libraries/experimental_log",
        f"{SDK_ROOT}/components/libraries/experimental_log/src",
        f"{SDK_ROOT}/components/libraries/experimental_memobj",
        f"{SDK_ROOT}/components/libraries/experimental_section_vars",
        f"{SDK_ROOT}/components/libraries/strerror",
        f"{SDK_ROOT}/components/libraries/pwr_mgmt",

        f"{SDK_ROOT}/external/fprintf",
    ]

    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
