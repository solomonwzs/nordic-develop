#!/bin/bash
set -euo pipefail

DIR="$(dirname $0)"
PREPARE="python3 $DIR/_helper/prepare.py"

bpids=()

function end() {
    if [ ${#bpids[@]} -ne 0 ]; then
        for pid in $bpids
        do
            kill $pid
        done
    fi
}
trap "end; exit" SIGINT SIGTERM

function rttlog() {
    JLinkExe -device NRF52 -if swd -speed 1000 -autoconnect 1 &
    bpids+=($!)
    sleep 1
    JLinkRTTClient
}

getopts "g:d:" OPT
case "$OPT" in
    g)
        $PREPARE $OPTARG
        ;;
    d)
        case $OPTARG in
            log)
                rttlog
                ;;
        esac
        ;;
esac

end
