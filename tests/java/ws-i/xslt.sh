#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

source $BASE_DIR/../common.sh

SAXON_HOME=$JLIB_DIR
SAXON=saxonb

java -classpath $SAXON_HOME/$SAXON-ant.jar:$SAXON_HOME/$SAXON-dom.jar:$SAXON_HOME/$SAXON-dom4j.jar:$SAXON_HOME/$SAXON-jdom.jar:$SAXON_HOME/$SAXON-s9api.jar:$SAXON_HOME/$SAXON-sql.jar:$SAXON_HOME/$SAXON-xom.jar:$SAXON_HOME/$SAXON-xpath.jar:$SAXON_HOME/$SAXON-xqj.jar:$SAXON_HOME/$SAXON.jar net.sf.saxon.Transform -s $2 -o $3 $1
