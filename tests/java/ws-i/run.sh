#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEMP_DIR=$BASE_DIR/tmp
BP12_DIR=$TEMP_DIR/bp12

source $BASE_DIR/../common.sh

cat $BASE_DIR/testlogtpl.xml | \
    grep -B 100 '***WSDL***' | \
    grep -v '***WSDL***' > $BASE_DIR/testlog.xml
cat $BASE_DIR/test.wsdl | grep -v '<?' >> $BASE_DIR/testlog.xml
cat $BASE_DIR/testlogtpl.xml | \
    grep -A 100 '***WSDL***' | \
    grep -v '***WSDL***' >> $BASE_DIR/testlog.xml

$BASE_DIR/xslt.sh \
    $BP12_DIR/tadriver.xsl \
    $BASE_DIR/testlog.xml \
    $BASE_DIR/report.xml
