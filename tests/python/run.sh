#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

unit2 discover -s $BASE_DIR/testcases/ -p *.py
