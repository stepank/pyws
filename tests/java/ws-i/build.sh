#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEST_DIR=$BASE_DIR/../..
TEMP_DIR=$BASE_DIR/tmp
BP12_DIR=$TEMP_DIR/bp12

$BASE_DIR/clean.sh

$TEST_DIR/get_wsdl.sh

mkdir $TEMP_DIR

wget http://ws-i.org/Profiles/BPTestToolsProcess-1.2-2.0-Final.zip

mv BPTestToolsProcess-1.2-2.0-Final.zip $BASE_DIR/wsi-test-tools.zip

unzip $BASE_DIR/wsi-test-tools.zip -d $TEMP_DIR

mkdir $BP12_DIR

unzip $TEMP_DIR/BPAnalyzer-1.2-Final.zip -d $BP12_DIR

$BASE_DIR/xslt.sh \
    $BP12_DIR/make-plugins.xsl \
    $BP12_DIR/BasicProfile-1.2.xml \
    $BP12_DIR/taplugins.xsl

cp $BP12_DIR/report.xsl $BASE_DIR/report.xsl
cp $BP12_DIR/common.xsl $BASE_DIR/common.xsl

rm -rf wsi-test-tools.zip
