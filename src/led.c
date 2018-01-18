#include "led.h"


static void
print_mac_address() {
  SEGGER_RTT_printf(0, "%x %x\n",
                    NRF_FICR->DEVICEADDR[0], NRF_FICR->DEVICEADDR[1]);
}


void
led_blinking() {
  bsp_board_leds_init();

  while (true) {
    for (int i = 0; i < LEDS_NUMBER; i++) {
      bsp_board_led_invert(i);
      nrf_delay_ms(500);

      print_mac_address();
    }
  }
}
