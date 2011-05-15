JLIB_DIR=/usr/share/java

CP=''
CP=$CP:$JLIB_DIR/wsdl4j.jar
CP=$CP:$JLIB_DIR/jaxrpc.jar
CP=$CP:$JLIB_DIR/commons-discovery.jar
CP=$CP:$JLIB_DIR/commons-logging-adapters.jar
CP=$CP:$JLIB_DIR/commons-logging-api.jar
CP=$CP:$JLIB_DIR/commons-logging.jar
CP=$CP:$JLIB_DIR/axis.jar
CP=$CP:$JLIB_DIR/junit4.jar
CP=$CP:$JLIB_DIR/hamcrest-core.jar
CP=$CP:$JLIB_DIR/activation.jar
CP=$CP:$JLIB_DIR/gnumail.jar

export JAVA_CP=$CP
