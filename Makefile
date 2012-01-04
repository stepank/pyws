ROOT_DIR=$(shell pwd)

include $(ROOT_DIR)/Makefile.common

all: test

develop:
	python setup.py develop

install:
	python setup.py install

test:
	make -C tests

clean:
	make -C tests clean

.PHONY: all develop install test clean
