#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEST_DIR=$BASE_DIR/../..

source $BASE_DIR/../common.sh

$BASE_DIR/clean.sh

$TEST_DIR/get_wsdl.sh

java -cp $JAVA_CP org.apache.axis.wsdl.WSDL2Java -o $BASE_DIR test.wsdl

javac -cp $JAVA_CP -d $BASE_DIR $BASE_DIR/TestServiceTestCase.java
