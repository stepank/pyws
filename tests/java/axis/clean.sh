#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

rm -rf $BASE_DIR/test.wsdl $BASE_DIR/com $BASE_DIR/testcases/*.class
