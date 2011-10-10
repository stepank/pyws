#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

if [ "$1" = "" ]; then
    PATTERN=*
else
    PATTERN=$1
fi;

unit2 discover -s $BASE_DIR/testcases/ -p $PATTERN.py
