ROOT_DIR=$(shell pwd)/../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common

build_local:
	php wsdl2php.php $(WSDL_FILE)

test:
	phpunit testcases

clean_local:
	rm -f TestService.php
