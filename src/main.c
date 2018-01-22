#include <string.h>
#include "led.h"
#include "ble_gap.h"
/* #include "ble_app.h" */

#define DEVICE "hello"

void
gap_params_init() {
  ret_code_t err_code;
  /* ble_gap_conn_params_t gap_conn_params; */
  ble_gap_conn_sec_mode_t sec_mode;

  /* ble_enable_params_t ble_enable_params; */
  /* memset(&ble_enable_params, 0, sizeof(ble_enable_params)); */
  /* ble_enable_params.gatts_enable_params.service_changed = APP_IS_SRVC_CHANGED_CHARACT_PRESENT; */
  /* err_code = sd_ble_enable(&ble_enable_params); */

  BLE_GAP_CONN_SEC_MODE_SET_OPEN(&sec_mode);
  err_code = sd_ble_gap_device_name_set(
      &sec_mode, (const uint8_t *)DEVICE, strlen(DEVICE));
  dlog("%d\n", err_code);
}


int
main(int argc, char **argv) {
  gap_params_init();
  led_blinking();
  // wait_key();

  return 0;
}
