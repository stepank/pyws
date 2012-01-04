ROOT_DIR=$(shell pwd)/../../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common
include $(TEST_DIR)/java/Makefile.common

TESTCASES=$(shell for f in `ls -1 testcases/*.java | grep -v TestService`; do \
    f=$${f:10}; \
    echo -n "testcases.$${f/.java/} "; \
done)

build_local:
	java -cp $(JAVA_CP) org.apache.axis.wsdl.WSDL2Java -a -o . test.wsdl
	javac -cp $(JAVA_CP) -d . testcases/*TestCase.java

test:
	java -cp $(CP) org.junit.runner.JUnitCore $(TESTCASES)

clean_local:
	rm -rf com testcases/*.class
