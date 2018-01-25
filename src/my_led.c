#include "boards.h"
#include "my_led.h"
#include "nrf_delay.h"


void
led_blinking() {
  bsp_board_leds_init();

  while (true) {
    for (int i = 0; i < LEDS_NUMBER; i++) {
      bsp_board_led_invert(i);
      nrf_delay_ms(500);
    }
  }
}
