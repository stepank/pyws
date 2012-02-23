ROOT_DIR=$(shell pwd)/../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common

CLASS_FILE=TestService.cs

#TESTCASES=$(shell for f in `ls -1 testcases/*.cs | grep -v TestService`; do \
#	f=$${f:10}; \
#	echo -n "testcases/$${f/.cs/.dll} "; \
#done)

$(CLASS_FILE):
	wsdl $(WSDL_FILE)

build_local: $(CLASS_FILE)
	gmcs -pkg:nunit -r:System.Web.Services -t:library TestService.cs testcases/*Test.cs

test:
	nunit-console -trace=Verbose TestService.dll

clean_local:
	rm -f $(CLASS_FILE) TestResult.xml TestService.dll testcases/*.dll
