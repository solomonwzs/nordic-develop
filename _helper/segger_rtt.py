#!/usr/bin/python3
# encoding: utf8

import common
from common import (
    SDK_ROOT,
)

__SRC = set([
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
    f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",
])

__INC = set([
    f"{SDK_ROOT}/external/segger_rtt",
])

def add_rtt_support():
    common.SRC_FILES.update(__SRC)
    common.INC_FOLDERS.update(__INC)
