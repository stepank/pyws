ROOT_DIR = $(shell pwd)
PYTHON ?= $(shell which python)
ENV ?= env

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

env:
	virtualenv $(ENV) -p $(PYTHON) --distribute
	source $(ENV)/bin/activate && \
	    make develop
	$(ENV)/bin/pip install $(HOST_FRAMEWORK)

jenkins: env
	source $(ENV)/bin/activate && \
	    make

clean_env:
	rm -rf $(ENV)

.PHONY: all develop install test clean jenkins clean_env
