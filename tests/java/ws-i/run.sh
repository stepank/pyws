#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

source $BASE_DIR/../common.sh

WSI_HOME=$BASE_DIR/wsi-test-tools

DEFAULT_WSI_HOME="${WSI_HOME}"

WSI_JAVA_HOME="${WSI_HOME}/java"

WSI_CP="${WSI_JAVA_HOME}/lib/wsi-test-tools.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib"

WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/xercesImpl.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/xmlParserAPIs.jar"

WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/wsdl4j.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/uddi4j.jar"

WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/axis.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/commons-discovery.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/commons-logging.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/saaj.jar"
WSI_CP="${WSI_CP}:${WSI_JAVA_HOME}/lib/jaxrpc.jar"

WSI_JAVA_OPTS="-Dorg.xml.sax.driver=org.apache.xerces.parsers.SAXParser"

java ${WSI_JAVA_OPTS} -Dwsi.home=${WSI_HOME} -cp ${WSI_CP} \
    org.wsi.test.analyzer.BasicProfileAnalyzer -config $BASE_DIR/config.xml