Development version
-------------------

* added adapters for Twisted Web and WSGI, issue #7,
* adapters report HTTP 500 response code on error, issue #4,
* examples and tests rely on pyws being installed (at least in dev mode),
* lots of automation (mainly for tests) using make files, issue #11,
* implemented WSDL wrapped document/literal style along with rpc/literal, the former is default, issue #12,
* WS-I BP 1.1 WSDL validation is back again (BP 1.2 validation is preserved),
* added headers validation, issue #15
* function docstrings are propagated to WSDL, issue #8,
* added python 2.5 support, issue #9.


Version 1.0
-----------

Common features:

* a web framework agnostic server,
* an adapter for Django,
* protocols: SOAP 1.1, REST, JSON,
* context handling & authentication framework,
* a simple types description system.

SOAP specific features:

* request, response, exceptions,
* automatic WSDL 1.1 service description generation, including headers and
  exceptions,
* simple types handling: integer, float, string, date, datetime,
* complex types handling: dict, list (nested structures of any depth are
  allowed),
* integration tests: PHP, Java (Axis 1.4), Python (suds), WS-I Basic Profile
  1.2.
