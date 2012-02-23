ROOT_DIR=$(shell pwd)/../../../..

include $(ROOT_DIR)/Makefile.common
include $(TEST_DIR)/Makefile.common
include $(TEST_DIR)/java/Makefile.common

TEMP_DIR=tmp
BP12_DIR=$(TEMP_DIR)/bp12

$(BP12_DIR):
	wget http://ws-i.org/Profiles/BPTestToolsProcess-1.2-2.0-Final.zip
	mv BPTestToolsProcess-1.2-2.0-Final.zip wsi-test-tools.zip
	mkdir -p $(BP12_DIR)
	unzip wsi-test-tools.zip -d $(TEMP_DIR)
	unzip $(TEMP_DIR)/BPAnalyzer-1.2-Final.zip -d $(BP12_DIR)
	rm -f wsi-test-tools.zip
	rm -f $(TEMP_DIR)/BPAnalyzer-1.2-Final.zip
	./xslt.sh $(JLIB_DIR) \
		$(BP12_DIR)/make-plugins.xsl \
		$(BP12_DIR)/BasicProfile-1.2.xml \
		$(BP12_DIR)/taplugins.xsl

common.xsl:
	cp $(BP12_DIR)/common.xsl common.xsl

report.xsl:
	cp $(BP12_DIR)/report.xsl report.xsl

build_local: $(BP12_DIR) common.xsl report.xsl

test:
	cat testlogtpl.xml | \
		grep -B 100 '***WSDL***' | \
		grep -v '***WSDL***' > testlog.xml
	cat test.wsdl | grep -v '<?' >> testlog.xml
	cat testlogtpl.xml | \
		grep -A 100 '***WSDL***' | \
		grep -v '***WSDL***' >> testlog.xml
	./xslt.sh $(JLIB_DIR) \
		$(BP12_DIR)/tadriver.xsl \
		testlog.xml \
		report.xml

clean_local:
	rm -rf testlog.xml $(TEMP_DIR)

clean_report:
	rm -f report.xml report.xsl common.xsl
