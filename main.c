#include <stdbool.h>

#include "boards.h"
#include "nrf.h"
#include "nrf_delay.h"
#include "SEGGER_RTT.h"


int
main(int argc, char **argv) {
  bsp_board_leds_init();

  while (true) {
    for (int i = 0; i < LEDS_NUMBER; i++) {
      bsp_board_led_invert(i);
      nrf_delay_ms(500);

      SEGGER_RTT_printf(0, "hello world\n");
    }
  }

  return 0;
}
