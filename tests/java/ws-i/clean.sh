#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

rm -rf $BASE_DIR/test.wsdl $BASE_DIR/report.xml $BASE_DIR/wsi-test-tools
