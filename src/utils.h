#ifndef __UTILS_H
#define __UTILS_H

#include <unistd.h>
#include "SEGGER_RTT.h"

#ifdef DEBUG
#   define dlog(_fmt_, ...) \
    SEGGER_RTT_printf(0, "\033[0;33m=%d= [%s:%d:%s]\033[0m " _fmt_, getpid(), \
                      __FILE__, __LINE__, __func__, ## __VA_ARGS__)
#else
#   define dlog(_fmt_, ...)
#endif

#endif
