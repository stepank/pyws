Welcome to pyws's documentation!
================================

Good day!

I hope this document will help you working with pyws. If you have any comments,
questions, suggestions, problems, or anything else to say, feel free to contact
me via email stepankk@gmail.com. pyws code is hosted on GitHub at
https://github.com/stepank/pyws.


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
* adapters for Django, Twisted Web, WSGI,
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
* integration tests: PHP, Java (Axis 1.4), Python (suds), C# (Mono),
* WS-I Basic Profile 1.1 and 1.2 validation.


.. _requirements:

Requirements
============

pyws itself depends only on python standard library and lxml. I've tested pyws
on all versions of python from 2.5 to 2.7. On python 2.5 pyws also requires
simplejson. For development pyws also requires unittest2 and suds.

pyws is written the way that it might be integrated with any web server and
python framework; it is achieved by using different adapters:

* :ref:`django_adapter` depends on Django, I use 1.5;
* :ref:`twisted_web_adapter` depends on Twisted, I use 11.0.0;
* :ref:`wsgi_adapter` depends on wsgiref, I use 0.1.2.


.. _installation:


Installation
============

The easiest way to install pyws is to run::

    easy_install pyws

Or you might download a source distribution archive from PyPI (available at
http://pypi.python.org/pypi/pyws) or clone the GIT repo. In these cases you
ought to change current directory to the root of pyws's distribution package
and run::

    make install

To install pyws in development mode (read more about `development mode
<http://packages.python.org/distribute/setuptools.html#development-mode>`_)::

    make develop

(They both actually run `python setup.py ...`.)


Changelog
=========

Version 1.1.4
-------------

* Fixed behaviour in case the tail starts with a slash, issue #32.
* Added support for Django up to 1.6, issue #33.


Version 1.1.3
-------------

* Added boolean support, issue #25.
* Added support for Django up to 1.5, issue #30.


Version 1.1.2
-------------

* Unicode support, issue #19.
* WSDL generator complains if some functions require context, but SOAP protocol
  does not have SOAP headers schema specified, issue #20.
* REST protocol retrieves arguments from request according to the
  specification, issue #21.
* Django adapter uses parse_qs to parse GET and POST arguments, issue #22.
* SOAP protocol returns dicts with fields ordered according to schema.
* JSON based protocols return date/datetime in ISO 8601 format.


Version 1.1.1
-------------

* Fixed pyws crashing if SOAP request body does not match the required schema,
  issue #16.
* Function arguments are inferred correctly, if they are not specified, issue
  #17.
* Running doctests returns exit code 1 in the case of failure, issue #18.


Version 1.1
-----------

* Adapters report HTTP 500 response code on error, issue #4.
* Added adapters for Twisted Web and WSGI, issue #7.
* Function docstrings are propagated to WSDL, issue #8.
* Added python 2.5 support, issue #9.
* Lots of automation (mainly for tests) using make files, issue #11.
* Implemented WSDL wrapped document/literal style along with rpc/literal,
  the former is default, issue #12.
* Added C# (Mono) integration tests, issue #13.
* WS-I BP 1.1 WSDL validation is back again (BP 1.2 validation is preserved).
* Added headers validation, issue #15.
* Examples and tests rely on pyws being installed (at least in dev mode).
* Added basic logging config to WSGI adapter example.
* Fixed some python suds tests.


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


Topics
======

.. toctree::
   :maxdepth: 3

   introduction
   complete_reference
   integration_tests
