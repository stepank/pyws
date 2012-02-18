ROOT_DIR=$(shell pwd)/../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common

WSDL_SUFFIX=?rpc=1

CLASS_FILE=TestService.cs

wsdl2php.php:
	wget https://raw.github.com/stepank/wsdl2php/master/src/bin/wsdl2php.php

$(CLASS_FILE): wsdl2php.php
	php -d html_errors=off wsdl2php.php $(WSDL_FILE)

build_local: $(CLASS_FILE)

test:
	phpunit testcases

clean_local:
	rm -f TestService.php wsdl2php.php
