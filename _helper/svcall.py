#!/usr/bin/python3
# encoding: utf8

from common import (
    SXXX,
    SDK_ROOT,
    list_union,
    DEVICE_LC,
)
import common


def add_svcall_as_func_support():
    _SRC = [
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/middleware/app_mw_ble_gap.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_gap_app.c",
        f"{SDK_ROOT}/components/serialization/common/ble_serialization.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/middleware/app_mw_nrf_soc.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/middleware/app_mw_ble_gatts.c",
        f"{SDK_ROOT}/components/serialization/application/transport/ser_softdevice_handler.c",
        f"{SDK_ROOT}/components/serialization/application/transport/ser_sd_transport.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/app_ble_gap_sec_keys.c",
        f"{SDK_ROOT}/components/serialization/common/cond_field_serialization.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_gap_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/nrf_soc_app.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_gatts_app.c",
        f"{SDK_ROOT}/components/serialization/common/transport/ser_hal_transport.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/nrf_soc_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/application/hal/ser_app_hal_nrf5x.c",
        f"{SDK_ROOT}/components/serialization/application/hal/ser_app_power_system_off.c",
        f"{SDK_ROOT}/components/drivers_nrf/clock/nrf_drv_clock.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_gap_evt_app.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_gattc_evt_app.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_gatts_evt_app.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_event.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_gatts_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_gattc_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/app_ble_user_mem.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_l2cap_evt_app.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_evt_app.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_gatt_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble/ble_l2cap_struct_serialization.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/middleware/app_mw_ble.c",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers/ble_app.c",

        f"{SDK_ROOT}/components/serialization/common/transport/ser_phy/ser_phy_uart.c",
        f"{SDK_ROOT}/components/drivers_nrf/uart/nrf_drv_uart.c",

        f"{SDK_ROOT}/components/libraries/queue/nrf_queue.c",
        f"{SDK_ROOT}/components/drivers_nrf/nrf_soc_nosd/nrf_soc.c",
        f"{SDK_ROOT}/components/drivers_nrf/common/nrf_drv_common.c",
    ]
    _INC = [
        f"{SDK_ROOT}/components/serialization/common",
        f"{SDK_ROOT}/components/serialization/application/codecs/ble/serializers",
        f"{SDK_ROOT}/components/serialization/application/transport",
        f"{SDK_ROOT}/components/serialization/common/struct_ser/ble",
        f"{SDK_ROOT}/components/serialization/application/hal",
        f"{SDK_ROOT}/components/serialization/common/transport",
        f"{SDK_ROOT}/components/serialization/common/transport/ser_phy",
        f"{SDK_ROOT}/components/serialization/common/transport/ser_phy/config",

        f"{SDK_ROOT}/components/drivers_nrf/clock",
        f"{SDK_ROOT}/components/drivers_nrf/uart",
        f"{SDK_ROOT}/components/drivers_nrf/common",
    ]
    _MACRO = [
        "SVCALL_AS_NORMAL_FUNCTION",
        "BLE_STACK_SUPPORT_REQD",
    ]

    list_union(common.SRC_FILES, _SRC)
    list_union(common.INC_FOLDERS, _INC)
    list_union(common.MACRO, _MACRO)
