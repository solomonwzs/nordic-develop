#include <string.h>

#include "ble_gap.h"
#include "my_init.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"
#include "utils.h"


void
log_init(void) {
    ret_code_t err_code = NRF_LOG_INIT(NULL);
    APP_ERROR_CHECK(err_code);

    NRF_LOG_DEFAULT_BACKENDS_INIT();
}


void
gap_params_init() {
  ret_code_t              err_code;
  ble_gap_conn_params_t   gap_conn_params;
  ble_gap_conn_sec_mode_t sec_mode;

  BLE_GAP_CONN_SEC_MODE_SET_OPEN(&sec_mode);

  dlog("init\n");
  err_code = sd_ble_gap_device_name_set(
      &sec_mode, (const uint8_t *)DEVICE_NAME, strlen(DEVICE_NAME));
  dlog("init\n");
  APP_ERROR_CHECK(err_code);

  memset(&gap_conn_params, 0, sizeof(gap_conn_params));

  gap_conn_params.min_conn_interval = MIN_CONN_INTERVAL;
  gap_conn_params.max_conn_interval = MAX_CONN_INTERVAL;
  gap_conn_params.slave_latency     = SLAVE_LATENCY;
  gap_conn_params.conn_sup_timeout  = CONN_SUP_TIMEOUT;

  err_code = sd_ble_gap_ppcp_set(&gap_conn_params);
  dlog("%d\n", err_code);
  APP_ERROR_CHECK(err_code);
}
