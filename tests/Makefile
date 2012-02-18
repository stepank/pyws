ROOT_DIR=$(shell pwd)/..

include $(ROOT_DIR)/Makefile.common

all: doc php python java mono

doc:
	python run_doctests.py

java:
	make -C java

mono:
	make -C mono

php:
	make -C php

python:
	make -C python

clean:
	make -C java clean
	make -C mono clean
	make -C php clean
	make -C python clean

.PHONY: all doc java mono php python clean
