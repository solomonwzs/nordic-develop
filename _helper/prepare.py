#!/usr/bin/python3
# encoding: utf8

import sys
from common import (
    generate_makefile,
    generate_vim_syntastic,
    generate_cscope,
    set_debug,
)
from segger_rtt import add_rtt_support
from socket import add_socket_support
from led import add_led_support
from log import add_log_support


if __name__ == "__main__":
    add_led_support()
    add_rtt_support()
    add_log_support()
    # add_socket_support()

    if len(sys.argv) > 1:
        if sys.argv[1] == "makefile":
            set_debug(False)
            generate_makefile()
        elif sys.argv[1] == "dmakefile":
            set_debug(True)
            generate_makefile()
        elif sys.argv[1] == "vim":
            generate_vim_syntastic()
        elif sys.argv[1] == "cscope":
            generate_cscope()
    else:
        set_debug(True)
        generate_makefile()
        generate_vim_syntastic()
        generate_cscope()
