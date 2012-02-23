ROOT_DIR=$(shell pwd)/../../../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common
include $(TEST_DIR)/java/Makefile.common

TEMP_DIR=tmp
BP11_DIR=$(TEMP_DIR)/bp11

WSI_HOME=$(BP11_DIR)/wsi-test-tools
DEFAULT_WSI_HOME=$(WSI_HOME)
WSI_JAVA_HOME=$(WSI_HOME)/java

JARS=wsi-test-tools.jar \
	xercesImpl.jar \
	xmlParserAPIs.jar \
	wsdl4j.jar \
	uddi4j.jar \
	axis.jar \
	commons-discovery.jar \
	commons-logging.jar \
	saaj.jar \
	jaxrpc.jar

WSI_CP=$(shell for j in $(JARS); do \
	echo -n "$(WSI_JAVA_HOME)/lib/$$j:"; \
done)

$(BP11_DIR):
	wget http://www.ws-i.org/Testing/Tools/2005/06/WSI_Test_Java_Final_1.1.zip
	mkdir -p $(BP11_DIR)
	mv WSI_Test_Java_Final_1.1.zip wsi-test-tools.zip
	unzip wsi-test-tools.zip -d $(BP11_DIR)
	rm -f wsi-test-tools.zip

common.xsl:
	cp $(BP11_DIR)/wsi-test-tools/common/xsl/common.xsl common.xsl

report.xsl:
	cp $(BP11_DIR)/wsi-test-tools/common/xsl/report.xsl report.xsl

build_local: $(BP11_DIR) common.xsl report.xsl

test:
	WSI_JAVA_OPTS="-Dorg.xml.sax.driver=org.apache.xerces.parsers.SAXParser"
	java $(WSI_JAVA_OPTS) -Dwsi.home=$(WSI_HOME) -cp $(WSI_CP) \
		org.wsi.test.analyzer.BasicProfileAnalyzer -config config.xml

clean_local:
	rm -rf $(TEMP_DIR) report.xml report.xsl common.xsl
