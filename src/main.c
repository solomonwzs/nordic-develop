#include <string.h>
#include "my_init.h"
#include "my_led.h"
#include "nrf_delay.h"
#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_nvic.h"
#include "utils.h"

void
print_mac_address() {
  uint8_t *p = (uint8_t *)&NRF_FICR->DEVICEADDR;
  dlog("%x:%x:%x:%x:%x:%x\n", p[5], p[4], p[3], p[2], p[1], p[0]);
}


void
wait_key() {
  char c = 0;
  while (true) {
    c = SEGGER_RTT_WaitKey();
    if (c == 'r') {
      SEGGER_RTT_printf(0, "%sResetting in %d second..%s\n",
                        RTT_CTRL_BG_BRIGHT_RED, 1, RTT_CTRL_RESET);
      nrf_delay_ms(1000);
      sd_nvic_SystemReset();
    }
  }
}


int
main(int argc, char **argv) {
  log_init();
  dlog("start...\n");
  timers_init();
  dlog("start...\n");
  scheduler_init();
  dlog("start...\n");
  ble_stack_init();
  dlog("start...\n");
  gap_params_init();
  dlog("start...\n");
  print_mac_address();
  led_blinking();
  // print_mac_address();

  return 0;
}
