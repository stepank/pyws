#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`
TEST_DIR=$BASE_DIR/../..

$BASE_DIR/clean.sh

$TEST_DIR/get_wsdl.sh
