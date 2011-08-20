#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEST_DIR=$BASE_DIR/../..

source $BASE_DIR/../common.sh

$BASE_DIR/clean.sh

$TEST_DIR/get_wsdl.sh

java -cp $JAVA_CP org.apache.axis.wsdl.WSDL2Java -a -o $BASE_DIR test.wsdl

javac -cp $JAVA_CP -d $BASE_DIR \
    $BASE_DIR/testcases/TestServiceTestCase.java \
    $BASE_DIR/testcases/NeedsAuthTestCase.java \
    $BASE_DIR/testcases/RaisesExceptionTestCase.java \
    $BASE_DIR/testcases/AddSimpleTestCase.java \
    $BASE_DIR/testcases/AddIntegersTestCase.java \
    $BASE_DIR/testcases/AddFloatsTestCase.java \
    $BASE_DIR/testcases/NextMonthTestCase.java \
    $BASE_DIR/testcases/AddStringDictsTestCase.java \
    $BASE_DIR/testcases/AddIntegerDictsTestCase.java \
    $BASE_DIR/testcases/AddStringListsTestCase.java \
    $BASE_DIR/testcases/AddIntegerListsTestCase.java \
    $BASE_DIR/testcases/SumTreeTestCase.java \
    $BASE_DIR/testcases/GetTreeTestCase.java
