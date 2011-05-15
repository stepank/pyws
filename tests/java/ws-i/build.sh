#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEST_DIR=$BASE_DIR/../..

$BASE_DIR/clean.sh

$TEST_DIR/get_wsdl.sh

wget http://www.ws-i.org/Testing/Tools/2005/06/WSI_Test_Java_Final_1.1.zip

mv WSI_Test_Java_Final_1.1.zip $BASE_DIR/wsi-test-tools.zip

unzip $BASE_DIR/wsi-test-tools.zip -d $BASE_DIR

rm -rf $BASE_DIR/wsi-test-tools.zip
