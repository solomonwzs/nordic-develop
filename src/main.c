#include <string.h>
#include "led.h"
#include "ble_gap.h"

#define DEVICE "hello"


/* void */
/* ble_stack_init() { */
/*   SOFTDEVICE_HANDLER_INIT(NRF_CLOCK_LFCLKSRC_XTAL_20_PPM, false); */
/* } */


int
main(int argc, char **argv) {
  led_blinking();
  // wait_key();

  return 0;
}
