ROOT_DIR=$(shell pwd)/../../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common
include $(TEST_DIR)/java/Makefile.common

CLASS_FILE=com

JARS=wsdl4j.jar \
	jaxrpc.jar \
	commons-discovery.jar \
	commons-logging-adapters.jar \
	commons-logging-api.jar \
	commons-logging.jar \
	axis.jar \
	junit4.jar \
	hamcrest-core.jar \
	activation.jar \
	gnumail.jar

JAVA_CP=$(shell for j in $(JARS); do \
	echo -n "$(JLIB_DIR)/$$j:"; \
done)

TESTCASES=$(shell for f in `ls -1 testcases/*.java | grep -v TestService`; do \
	f=$${f:10}; \
	echo -n "testcases.$${f/.java/} "; \
done)

$(CLASS_FILE):
	java -cp $(JAVA_CP) org.apache.axis.wsdl.WSDL2Java -a -o . $(WSDL_FILE)

build_local: $(CLASS_FILE)
	javac -cp $(JAVA_CP) -d . testcases/*TestCase.java

test:
	java -cp $(JAVA_CP) org.junit.runner.JUnitCore $(TESTCASES)

clean_local:
	rm -rf $(CLASS_FILE) testcases/*.class
