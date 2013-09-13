Version 1.1.4
-------------

* Added support for Django up to 1.6, issue #33.


Version 1.1.3
-------------

* Added boolean support, issue #25.
* Added support for Django up to 1.5, issue #30.


Version 1.1.2
-------------

* Unicode support, issue #19,
* WSDL generator complains if some functions require context, but SOAP protocol
  does not have SOAP headers schema specified, issue #20,
* REST protocol retrieves arguments from request according to the
  specification, issue #21,
* Django adapter uses parse_qs to parse GET and POST arguments, issue #22,
* SOAP protocol returns dicts with fields ordered according to schema,
* JSON based protocols return date/datetime in ISO 8601 format.



Version 1.1.1
-------------

* fixed pyws crashing if SOAP request body does not match the required schema,
  issue #16,
* function arguments are inferred correctly, if they are not specified, issue
  #17,
* running doctests returns exit code 1 in the case of failure, issue #18.


Version 1.1
-----------

* adapters report HTTP 500 response code on error, issue #4,
* added adapters for Twisted Web and WSGI, issue #7,
* function docstrings are propagated to WSDL, issue #8,
* added python 2.5 support, issue #9,
* lots of automation (mainly for tests) using make files, issue #11,
* implemented WSDL wrapped document/literal style along with rpc/literal,
  the former is default, issue #12,
* added C# (Mono) integration tests, issue #13,
* WS-I BP 1.1 WSDL validation is back again (BP 1.2 validation is preserved),
* added headers validation, issue #15,
* examples and tests rely on pyws being installed (at least in dev mode),
* added basic logging config to WSGI adapter example,
* fixed some python suds tests.


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
