Overview
========

Pyws is a project, which purpuse is to help developers to expose some functions
of their systems as public APIs via SOAP with WSDL description. The main idea
is to let developers completely forget about SOAP itself and make creating of
APIs fast and painless.

After you integrate pyws with your project, you'll be able to generate WSDL
description of your public API. When someone wants to use the API, all you need
to do is to give him a link to WSDL description of the service. Using this
description, anyone can easily call your functions remotely via SOAP and he
won't need to bother himself with generating XML, sending requests manually
via HTTP, parsing responses and so on. pyws will take care of processing
requests on the server and numerous SOAP clients are at your disposal to send
requests and process responces.


What is already implemented
---------------------------

Common features:

* a web framework agnostic server,
* an adapter for Django,
* protocols: SOAP 1.1, REST, JSON,
* context handling & authentication framework,
* a simple types description system.

SOAP specific features:

* request, response, exceptions,
* WSDL 1.1 service description, including headers and exceptions,
* simple types handling: integer, float, string, date, datetime,
* complex types handling: dict, list (nested structures of any depth are
  allowed),
* integration tests: PHP, Java (Axis 1.4), WS-I Basic Profile 1.2.


What will be done next
----------------------

* installation script and instructions,
* maybe, declarative function arguments description (smth like Django models),
* other `issues <https://github.com/stepank/pyws/issues>`_.
