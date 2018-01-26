#include <string.h>

#include "app_scheduler.h"
#include "app_timer.h"
#include "ble_cts_c.h"
#include "ble_gap.h"
#include "bsp.h"
#include "my_init.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"
#include "nrf_sdh.h"
#include "nrf_sdh_ble.h"
#include "peer_manager.h"
#include "utils.h"

#define APP_BLE_CONN_CFG_TAG 1
#define APP_BLE_OBSERVER_PRIO 3
#define SCHED_MAX_EVENT_DATA_SIZE APP_TIMER_SCHED_EVENT_DATA_SIZE
#define SECURITY_REQUEST_DELAY APP_TIMER_TICKS(4000)

#ifdef SVCALL_AS_NORMAL_FUNCTION
#   define SCHED_QUEUE_SIZE 20
#else
#   define SCHED_QUEUE_SIZE 10
#endif


APP_TIMER_DEF(m_sec_req_timer_id);
BLE_CTS_C_DEF(m_cts_c);

static uint16_t m_cur_conn_handle = BLE_CONN_HANDLE_INVALID;


static void sec_req_timeout_handler(void *);
static void ble_evt_handler(ble_evt_t const *, void *);


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

static void
sec_req_timeout_handler(void * p_context) {
  ret_code_t           err_code;
  pm_conn_sec_status_t status;

  if (m_cur_conn_handle != BLE_CONN_HANDLE_INVALID) {
    err_code = pm_conn_sec_status_get(m_cur_conn_handle, &status);
    APP_ERROR_CHECK(err_code);

    // If the link is still not secured by the peer,
    // initiate security procedure.
    if (!status.encrypted) {
      err_code = pm_conn_secure(m_cur_conn_handle, false);
      APP_ERROR_CHECK(err_code);
    }
  }
}


void
timers_init() {
  ret_code_t err_code;

  err_code = app_timer_init();
  APP_ERROR_CHECK(err_code);

  // Create security request timer.
  err_code = app_timer_create(&m_sec_req_timer_id,
                              APP_TIMER_MODE_SINGLE_SHOT,
                              sec_req_timeout_handler);
  APP_ERROR_CHECK(err_code);
}


void
scheduler_init() {
    APP_SCHED_INIT(SCHED_MAX_EVENT_DATA_SIZE, SCHED_QUEUE_SIZE);
}


void
ble_stack_init() {
  ret_code_t err_code;

  dlog("start...\n");
  err_code = nrf_sdh_enable_request();
  APP_ERROR_CHECK(err_code);

  // Configure the BLE stack using the default settings.
  // Fetch the start address of the application RAM.
  uint32_t ram_start = 0;
  dlog("start...\n");
  err_code = nrf_sdh_ble_default_cfg_set(APP_BLE_CONN_CFG_TAG, &ram_start);
  dlog("start...\n");
  APP_ERROR_CHECK(err_code);

  // Enable BLE stack.
  err_code = nrf_sdh_ble_enable(&ram_start);
  APP_ERROR_CHECK(err_code);

  // Register a handler for BLE events.
  NRF_SDH_BLE_OBSERVER(m_ble_observer, APP_BLE_OBSERVER_PRIO,
                       ble_evt_handler, NULL);
}


static void
ble_evt_handler(ble_evt_t const * p_ble_evt, void * p_context) {
  ret_code_t err_code;

  switch (p_ble_evt->header.evt_id) {
    case BLE_GAP_EVT_CONNECTED:
      dlog("Connected.");
      err_code = bsp_indication_set(BSP_INDICATE_CONNECTED);
      APP_ERROR_CHECK(err_code);
      m_cur_conn_handle = p_ble_evt->evt.gap_evt.conn_handle;
      err_code = app_timer_start(m_sec_req_timer_id,
                                 SECURITY_REQUEST_DELAY, NULL);
      APP_ERROR_CHECK(err_code);
      break;

    case BLE_GAP_EVT_DISCONNECTED:
      dlog("Disconnected.");
      m_cur_conn_handle = BLE_CONN_HANDLE_INVALID;
      if (p_ble_evt->evt.gap_evt.conn_handle == m_cts_c.conn_handle) {
        m_cts_c.conn_handle = BLE_CONN_HANDLE_INVALID;
      }
      break; // BLE_GAP_EVT_DISCONNECTED

#ifndef S140
    case BLE_GAP_EVT_PHY_UPDATE_REQUEST: {
      dlog("PHY update request.");
      ble_gap_phys_t const phys = {
        .rx_phys = BLE_GAP_PHY_AUTO,
        .tx_phys = BLE_GAP_PHY_AUTO,
      };
      err_code = sd_ble_gap_phy_update(
          p_ble_evt->evt.gap_evt.conn_handle, &phys);
      APP_ERROR_CHECK(err_code);
    } break;
#endif

    case BLE_GATTC_EVT_TIMEOUT:
      // Disconnect on GATT Client timeout event.
      dlog("GATT Client Timeout.");
      err_code = sd_ble_gap_disconnect(
          p_ble_evt->evt.gattc_evt.conn_handle,
          BLE_HCI_REMOTE_USER_TERMINATED_CONNECTION);
      APP_ERROR_CHECK(err_code);
      break;

    case BLE_GATTS_EVT_TIMEOUT:
      // Disconnect on GATT Server timeout event.
      dlog("GATT Server Timeout.");
      err_code = sd_ble_gap_disconnect(
          p_ble_evt->evt.gatts_evt.conn_handle,
          BLE_HCI_REMOTE_USER_TERMINATED_CONNECTION);
      APP_ERROR_CHECK(err_code);
      break;

    default:
      // No implementation needed.
      break;
  }
}
