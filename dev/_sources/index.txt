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
simplejson.

pyws is written the way that it might be integrated with any web server and
python framework; it is achieved by using different adapters:

* :ref:`django_adapter` depends on Django, I use 1.3;
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


Topics
======

.. toctree::
   :maxdepth: 3

   introduction
   complete_reference
   integration_tests
