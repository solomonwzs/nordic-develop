# vim: noet:

include _makefile/Makefile.common

$(OUTPUT_DIRECTORY)/$(TARGETS).out: LINKER_SCRIPT := $(LINKER_SCRIPT)

include _makefile/Makefile.src

include _makefile/Makefile.inc

include _makefile/Makefile.flags

include _makefile/Makefile.lib

.PHONY: default

default: $(TARGETS)

include $(TEMPLATE_PATH)/Makefile.common

$(foreach target, $(TARGETS), $(call define_target, $(target)))

.PHONY: flash flash_softdevice erase

# Flash the program
flash: $(OUTPUT_DIRECTORY)/$(TARGETS).hex
	@echo Flashing: $<
	nrfjprog -f nrf52 --program $< --sectorerase
	nrfjprog -f nrf52 --reset

# Flash softdevice
flash_softdevice:
	@echo Flashing: s112_nrf52810_5.1.0_softdevice.hex
	nrfjprog -f nrf52 --program $(SDK_ROOT)/components/softdevice/s112/hex/s112_nrf52810_5.1.0_softdevice.hex --sectorerase
	nrfjprog -f nrf52 --reset

erase:
	nrfjprog -f nrf52 --eraseall
