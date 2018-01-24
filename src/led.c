#include "led.h"


void
print_mac_address() {
  dlog("%x %x\n", NRF_FICR->DEVICEADDR[0], NRF_FICR->DEVICEADDR[1]);
}


void
led_blinking() {
  bsp_board_leds_init();

  while (true) {
    for (int i = 0; i < LEDS_NUMBER; i++) {
      bsp_board_led_invert(i);
      nrf_delay_ms(500);

      // print_mac_address();
    }
  }
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
