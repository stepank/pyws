#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

rm -rf \
    $BASE_DIR/test.wsdl \
    $BASE_DIR/testlog.xml \
    $BASE_DIR/report.xml \
    $BASE_DIR/report.xsl \
    $BASE_DIR/common.xsl \
    $BASE_DIR/tmp
