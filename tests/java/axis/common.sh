export JAVA_DIR=/usr/share/java

CP=''
CP=$CP:$JAVA_DIR/wsdl4j.jar
CP=$CP:$JAVA_DIR/jaxrpc.jar
CP=$CP:$JAVA_DIR/commons-discovery.jar
CP=$CP:$JAVA_DIR/commons-logging-adapters.jar
CP=$CP:$JAVA_DIR/commons-logging-api.jar
CP=$CP:$JAVA_DIR/commons-logging.jar
CP=$CP:$JAVA_DIR/axis.jar
CP=$CP:$JAVA_DIR/junit4.jar
CP=$CP:$JAVA_DIR/hamcrest-core.jar
CP=$CP:$JAVA_DIR/activation.jar
CP=$CP:$JAVA_DIR/gnumail.jar

export JAVA_CP=$CP