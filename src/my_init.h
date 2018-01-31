#ifndef __MY_INIT_H
#define __MY_INIT_H

#include <stdbool.h>

extern void log_init();

extern void timers_init();

extern void buttons_leds_init(bool *p_erase_bonds);

extern void ble_stack_init();

extern void gap_params_init();

extern void gatt_init();

extern void advertising_init();

extern void services_init();

extern void conn_params_init();

extern void peer_manager_init();

extern void application_timers_start();

extern void advertising_start(bool erase_bonds);

extern void power_manage();

#endif
