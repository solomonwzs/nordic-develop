#!/usr/bin/python3
# encoding: utf8

import common
from common import (
    SDK_ROOT,
    list_union,
)

__SRC = [
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",
]

__INC = [
    f"{SDK_ROOT}/external/segger_rtt",
]

def add_rtt_support():
    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
