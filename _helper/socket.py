#!/usr/bin/python3
# encoding: utf8

from common import (
    SXXX,
    SDK_ROOT,
    list_union,
)
import common


def add_socket_support():
    __SRC = [
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_rtt.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_serial.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_backend_uart.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_default_backends.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_frontend.c",
        f"{SDK_ROOT}/components/libraries/experimental_log/src/nrf_log_str_formatter.c",
        f"{SDK_ROOT}/components/libraries/button/app_button.c",
        f"{SDK_ROOT}/components/libraries/util/app_error.c",
        f"{SDK_ROOT}/components/libraries/util/app_error_weak.c",
        f"{SDK_ROOT}/components/libraries/scheduler/app_scheduler.c",
        f"{SDK_ROOT}/components/libraries/timer/app_timer.c",
        f"{SDK_ROOT}/components/libraries/util/app_util_platform.c",
        f"{SDK_ROOT}/components/libraries/hardfault/hardfault_implementation.c",
        f"{SDK_ROOT}/components/libraries/mem_manager/mem_manager.c",
        f"{SDK_ROOT}/components/libraries/util/nrf_assert.c",
        f"{SDK_ROOT}/components/libraries/atomic_fifo/nrf_atfifo.c",
        f"{SDK_ROOT}/components/libraries/balloc/nrf_balloc.c",
        f"{SDK_ROOT}/external/fprintf/nrf_fprintf.c",
        f"{SDK_ROOT}/external/fprintf/nrf_fprintf_format.c",
        f"{SDK_ROOT}/components/libraries/experimental_memobj/nrf_memobj.c",
        f"{SDK_ROOT}/components/libraries/experimental_section_vars/nrf_section_iter.c",
        f"{SDK_ROOT}/components/libraries/strerror/nrf_strerror.c",
        f"{SDK_ROOT}/external/lwip/src/core/def.c",
        f"{SDK_ROOT}/external/lwip/src/core/dhcp.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/dhcp6.c",
        f"{SDK_ROOT}/external/lwip/src/core/dns.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv4/icmp.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/icmp6.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/inet6.c",
        f"{SDK_ROOT}/external/lwip/src/core/inet_chksum.c",
        f"{SDK_ROOT}/external/lwip/src/core/init.c",
        f"{SDK_ROOT}/external/lwip/src/core/ip.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv4/ip4.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv4/ip4_addr.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/ip6.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/ip6_addr.c",
        f"{SDK_ROOT}/external/lwip/src/core/memp.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/mld6.c",
        f"{SDK_ROOT}/external/lwip/src/core/ipv6/nd6.c",
        f"{SDK_ROOT}/external/lwip/src/core/netif.c",
        f"{SDK_ROOT}/external/lwip/src/port/nrf_platform_port.c",
        f"{SDK_ROOT}/external/lwip/src/core/pbuf.c",
        f"{SDK_ROOT}/external/lwip/src/core/raw.c",
        f"{SDK_ROOT}/external/lwip/src/core/sys.c",
        f"{SDK_ROOT}/external/lwip/src/core/tcp.c",
        f"{SDK_ROOT}/external/lwip/src/core/tcp_in.c",
        f"{SDK_ROOT}/external/lwip/src/core/tcp_out.c",
        f"{SDK_ROOT}/external/lwip/src/core/timeouts.c",
        f"{SDK_ROOT}/external/lwip/src/core/udp.c",
        f"{SDK_ROOT}/components/boards/boards.c",
        f"{SDK_ROOT}/components/drivers_nrf/clock/nrf_drv_clock.c",
        f"{SDK_ROOT}/components/drivers_nrf/common/nrf_drv_common.c",
        f"{SDK_ROOT}/components/drivers_nrf/gpiote/nrf_drv_gpiote.c",
        f"{SDK_ROOT}/components/drivers_nrf/uart/nrf_drv_uart.c",
        f"{SDK_ROOT}/components/softdevice/common/nrf_sdh.c",
        f"{SDK_ROOT}/components/softdevice/common/nrf_sdh_ble.c",
        f"{SDK_ROOT}/components/softdevice/common/nrf_sdh_soc.c",
        f"{SDK_ROOT}/components/libraries/bsp/bsp.c",
        f"{SDK_ROOT}/components/libraries/bsp/bsp_nfc.c",
        f"{SDK_ROOT}/components/ble/common/ble_advdata.c",
        f"{SDK_ROOT}/components/ble/common/ble_srv_common.c",
        f"{SDK_ROOT}/components/iot/ble_6lowpan/ble_6lowpan.c",
        f"{SDK_ROOT}/components/iot/socket/config/medium/config_medium.c",
        f"{SDK_ROOT}/components/iot/errno/errno.c",
        f"{SDK_ROOT}/components/iot/socket/libraries/addr_util/inet_pton.c",
        f"{SDK_ROOT}/components/iot/context_manager/iot_context_manager.c",
        f"{SDK_ROOT}/components/iot/medium/ipv6_medium_ble.c",
        f"{SDK_ROOT}/components/iot/ipv6_parse/ipv6_parse.c",
        f"{SDK_ROOT}/components/iot/socket/libraries/mbuf/mbuf.c",
        f"{SDK_ROOT}/components/iot/socket/libraries/fifo/nrf_fifo.c",
        f"{SDK_ROOT}/components/iot/socket/libraries/portdb/portdb.c",
        f"{SDK_ROOT}/components/iot/socket/common/sleep.c",
        f"{SDK_ROOT}/components/iot/socket/common/socket.c",
        f"{SDK_ROOT}/components/iot/socket/platform/ble/socket_ble.c",
        f"{SDK_ROOT}/components/iot/socket/transport/lwip/transport_handler.c",
        f"{SDK_ROOT}/components/toolchain/gcc/gcc_startup_nrf52.S",
        f"{SDK_ROOT}/components/toolchain/system_nrf52.c",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ipsp/ble_ipsp.c",
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT.c",
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c",
        f"{SDK_ROOT}/external/segger_rtt/SEGGER_RTT_printf.c",
    ]

    __INC = [
        f"inc/socket",
        f"{SDK_ROOT}/components/iot/errno",
        f"{SDK_ROOT}/components/iot/socket/transport/lwip",
        f"{SDK_ROOT}/components/libraries/csense_drv",
        f"{SDK_ROOT}/components/ble/ble_services/ble_tps",
        f"{SDK_ROOT}/components/iot/socket/config/medium",
        f"{SDK_ROOT}/components/drivers_nrf/rng",
        f"{SDK_ROOT}/components/libraries/experimental_log/src",
        f"{SDK_ROOT}/components/drivers_nrf/usbd",
        f"{SDK_ROOT}/components/toolchain/gcc",
        f"{SDK_ROOT}/components/ble/ble_services/ble_dis",
        f"{SDK_ROOT}/components/drivers_nrf/pwm",
        f"{SDK_ROOT}/components/drivers_nrf/uart",
        f"{SDK_ROOT}/components/drivers_nrf/hal",
        f"{SDK_ROOT}/components/libraries/crc16",
        f"{SDK_ROOT}/components/drivers_nrf/twi_master",
        f"{SDK_ROOT}/components/ble/ble_services/ble_cts_c",
        f"{SDK_ROOT}/components/drivers_nrf/saadc",
        f"{SDK_ROOT}/components/drivers_nrf/gpiote",
        f"{SDK_ROOT}/components/drivers_nrf/i2s",
        f"{SDK_ROOT}/components/libraries/cli",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ias",
        f"{SDK_ROOT}/components/libraries/low_power_pwm",
        f"{SDK_ROOT}/components/toolchain",
        f"{SDK_ROOT}/components/libraries/hci",
        f"{SDK_ROOT}/components/drivers_nrf/spi_slave",
        f"{SDK_ROOT}/components/ble/ble_services/ble_hrs",
        f"{SDK_ROOT}/components/libraries/hardfault",
        f"{SDK_ROOT}/components/softdevice/common",
        f"{SDK_ROOT}/components/ble/ble_services/ble_nus",
        f"{SDK_ROOT}/components/libraries/experimental_log",
        f"{SDK_ROOT}/components/ble/ble_services/ble_nus_c",
        f"{SDK_ROOT}/components/libraries/mem_manager",
        f"{SDK_ROOT}/components/libraries/fstorage",
        f"{SDK_ROOT}/external/lwip/src/include/lwip",
        f"{SDK_ROOT}/components/iot/socket/common",
        f"{SDK_ROOT}/components/drivers_nrf/wdt",
        f"{SDK_ROOT}/components/libraries/crc32",
        f"{SDK_ROOT}/components/libraries/fds",
        f"{SDK_ROOT}/components/libraries/usbd/class/hid/mouse",
        f"{SDK_ROOT}/components/libraries/pwm",
        f"{SDK_ROOT}/components/libraries/strerror",
        f"{SDK_ROOT}/components/iot/ipv6_parse",
        f"{SDK_ROOT}/components/drivers_nrf/power",
        f"{SDK_ROOT}/components/libraries/usbd/class/msc",
        f"{SDK_ROOT}/components/libraries/gpiote",
        f"{SDK_ROOT}/components/libraries/experimental_memobj",
        f"{SDK_ROOT}/components/softdevice/{SXXX}/headers/nrf52",
        f"{SDK_ROOT}/components/ble/nrf_ble_qwr",
        f"{SDK_ROOT}/components/ble/ble_services/ble_rscs_c",
        f"{SDK_ROOT}/components/libraries/usbd/class/cdc",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ipsp",
        f"{SDK_ROOT}/components/libraries/uart",
        f"{SDK_ROOT}/components/iot/medium",
        f"{SDK_ROOT}/components/ble/ble_services/ble_rscs",
        f"{SDK_ROOT}/components/iot/ble_6lowpan",
        f"{SDK_ROOT}/components/libraries/csense",
        f"{SDK_ROOT}/components/drivers_nrf/common",
        f"{SDK_ROOT}/components/libraries/usbd/class/hid/generic",
        f"{SDK_ROOT}/external/segger_rtt",
        f"{SDK_ROOT}/components/drivers_nrf/pdm",
        f"{SDK_ROOT}/external/lwip/src/port",
        f"{SDK_ROOT}/components/libraries/slip",
        f"{SDK_ROOT}/components/libraries/mutex",
        f"{SDK_ROOT}/components/drivers_nrf/comp",
        f"{SDK_ROOT}/components/iot/socket/platform/ble",
        f"{SDK_ROOT}/components/libraries/timer",
        f"{SDK_ROOT}/components/ble/ble_services/ble_lls",
        f"{SDK_ROOT}/components/iot/socket/libraries/portdb",
        f"{SDK_ROOT}/components/softdevice/{SXXX}/headers",
        f"{SDK_ROOT}/components/ble/ble_services/ble_bas",
        f"{SDK_ROOT}/components/ble/ble_services/ble_cscs",
        f"{SDK_ROOT}/external/lwip/src/include",
        f"{SDK_ROOT}/components/libraries/twi",
        f"{SDK_ROOT}/components/device",
        f"{SDK_ROOT}/components/libraries/usbd/class/hid/kbd",
        f"{SDK_ROOT}/components/libraries/experimental_section_vars",
        f"{SDK_ROOT}/components/libraries/atomic_fifo",
        f"{SDK_ROOT}/components/libraries/queue",
        f"{SDK_ROOT}/components/boards",
        f"{SDK_ROOT}/components/drivers_nrf/lpcomp",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ias_c",
        f"{SDK_ROOT}/components/libraries/button",
        f"{SDK_ROOT}/components/ble/ble_advertising",
        f"{SDK_ROOT}/components/ble/ble_racp",
        f"{SDK_ROOT}/components/libraries/usbd/config",
        f"{SDK_ROOT}/components/libraries/usbd/class/audio",
        f"{SDK_ROOT}/components/libraries/ecc",
        f"{SDK_ROOT}/components/ble/ble_services/ble_dfu",
        f"{SDK_ROOT}/external/fprintf",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ans_c",
        f"{SDK_ROOT}/components/drivers_nrf/timer",
        f"{SDK_ROOT}/components/libraries/twi_mngr",
        f"{SDK_ROOT}/components/iot/common",
        f"{SDK_ROOT}/components/iot/context_manager",
        f"{SDK_ROOT}/components/ble/ble_services/ble_lbs_c",
        f"{SDK_ROOT}/external/lwip/src/port/arch",
        f"{SDK_ROOT}/components/drivers_nrf/delay",
        f"{SDK_ROOT}/components/ble/ble_services/ble_bas_c",
        f"{SDK_ROOT}/components/libraries/usbd/class/cdc/acm",
        f"{SDK_ROOT}/components/ble/ble_services/ble_gls",
        f"{SDK_ROOT}/components/drivers_nrf/twis_slave",
        f"{SDK_ROOT}/components/ble/peer_manager",
        f"{SDK_ROOT}/components/drivers_nrf/swi",
        f"{SDK_ROOT}/components/drivers_nrf/spi_master",
        f"{SDK_ROOT}/external/lwip/src/include/netif",
        f"{SDK_ROOT}/components/iot/socket/libraries/mbuf",
        f"{SDK_ROOT}/components/ble/ble_services/ble_ancs_c",
        f"{SDK_ROOT}/components/ble/ble_services/ble_hrs_c",
        f"{SDK_ROOT}/components/iot/socket/libraries/fifo",
        f"{SDK_ROOT}/components/libraries/scheduler",
        f"{SDK_ROOT}/components/libraries/usbd/class/hid",
        f"{SDK_ROOT}/components/drivers_nrf/qdec",
        f"{SDK_ROOT}/components/drivers_nrf/ppi",
        f"{SDK_ROOT}/components/libraries/bsp",
        f"{SDK_ROOT}/components/ble/common",
        f"{SDK_ROOT}/components/drivers_nrf/clock",
        f"{SDK_ROOT}/components/iot/socket/api",
        f"{SDK_ROOT}/components/ble/ble_services/ble_hids",
        f"{SDK_ROOT}/components/libraries/balloc",
        f"{SDK_ROOT}/components/libraries/util",
        f"{SDK_ROOT}/components/drivers_nrf/rtc",
        f"{SDK_ROOT}/components",
        f"{SDK_ROOT}/components/libraries/led_softblink",
        f"{SDK_ROOT}/components/ble/ble_services/ble_hts",
        f"{SDK_ROOT}/components/ble/ble_services/ble_lbs",
        f"{SDK_ROOT}/components/libraries/usbd",
        f"{SDK_ROOT}/components/libraries/atomic",
        f"{SDK_ROOT}/components/toolchain/cmsis/include",
        f"{SDK_ROOT}/components/ble/ble_dtm",
    ]

    __M = [
        "BLE_STACK_SUPPORT_REQD",
        "CONFIG_GPIO_AS_PINRESET",
        "ENABLE_DEBUG_LOG_SUPPORT",
        "FLOAT_ABI_HARD",
        "LWIP_DONT_PROVIDE_BYTEORDER_FUNCTIONS",
        "NRF52_PAN_74",
        "NRF_SD_BLE_API_VERSION=5",
        "RETARGET_ENABLED=1",
        "S132",
        "SDK_MUTEX_ENABLE",
        "SOFTDEVICE_PRESENT",
        "SWI_DISABLE0",
        "__HEAP_SIZE=0",
    ]

    list_union(common.SRC_FILES, __SRC)
    list_union(common.INC_FOLDERS, __INC)
    list_union(common.MACRO, __M)
    common.SDK_CONFIG_FILE = "./config/socket/sdk_config.h"
    common.BOARD = "BOARD_PCA10040"
    common.LINKER_SCRIPT = "./ld/socket/iot_socket_tcp_client_gcc_nrf52.ld"
    common.SOFTDEVICE = f"{common.SDK_ROOT}/components/softdevice/s132/hex/s132_nrf52_5.0.0_softdevice.hex"
