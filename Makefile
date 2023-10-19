# Makefile for use with Android's kernel/build system
KBUILD_OPTIONS += AURIX_CAN_KERNEL_ROOT=$(shell pwd)
KBUILD_OPTIONS += KERNEL_ROOT=$(ROOT_DIR)/$(KERNEL_DIR)
KBUILD_OPTIONS += MODNAME=aurix-can
QTI_CAN_BLD_DIR := $(TOP)/vendor/qcom/opensource/aurix-can-kernel/

M=$(shell pwd)

all: modules

modules:
	$(MAKE) -C $(KERNEL_SRC) M=$(M) modules $(KBUILD_OPTIONS)

modules_install:
	$(MAKE) -C $(KERNEL_SRC) M=$(M) modules_install

clean:
	$(MAKE) -C $(KERNEL_SRC) M=$(M) clean
