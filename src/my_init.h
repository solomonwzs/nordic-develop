#ifndef __MY_INIT_H
#define __MY_INIT_H

#include "app_util.h"

#define DEVICE_NAME "hello-ble"

// Minimum acceptable connection interval
#define MIN_CONN_INTERVAL MSEC_TO_UNITS(500, UNIT_1_25_MS)

// Maximum acceptable connection interval
#define MAX_CONN_INTERVAL MSEC_TO_UNITS(1000, UNIT_1_25_MS)

// Slave latency.
#define SLAVE_LATENCY 0

// Connection supervisory time-out
#define CONN_SUP_TIMEOUT MSEC_TO_UNITS(4000, UNIT_10_MS)

extern void gap_params_init();

extern void log_init();

extern void timers_init();

extern void scheduler_init();

extern void ble_stack_init();

#endif
