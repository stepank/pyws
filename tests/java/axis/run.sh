#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

source $BASE_DIR/common.sh

java -cp $CP org.junit.runner.JUnitCore TestServiceTestCase