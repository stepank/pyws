Getting started, part 1
=======================

In this tutorial we are going to install pyws SOAP server providing WSDL,
add there some functions and test it.


Environment
-----------

pyws itself depends only on python standard library and lxml. I've tested pyws
mainly on python 2.6.

pyws is written the way that it might be integrated with any web server and
python framework; it is achieved by using different adapters. However, at
present, the only existing adapter is the one for Django. Therefore, of course,
we need to have Django installed, I use Django 1.3.

Also pyws root directory (i.e. the one containing ``examples``, ``src`` and
``tests`` directories) should be the part of your ``PYTHONPATH``. If you use
bash, then this should work::

    export PYTHONPATH=/path/to/pyws/root/directory

For testing purposes we'll use curl.


Project
-------

Let's create a new Django project::

    $ django-admin startproject pywstest
    $ cd !$

Here we will create a file ``server.py``, which we are going to edit::

    $ touch server.py

NOTE: You need to turn off ``django.middleware.csrf.CsrfViewMiddleware`` in
``settings.py``, otherwise you may encounter problems.


Some code
---------

Open file ``server.py`` in your favorite editor and let's start coding. First
of all, we need to import ``SoapServer`` class::

    from pyws.server import SoapServer

Next, we create a server::

    server = SoapServer(
        service_name='Test',
        tns='http://example.com/',
        location='http://localhost:8000/api/',
    )

Some explatations about the arguments would be useful:

#. ``service_name`` gives a name to our server, it is used to generate a WSDL
   description.
#. ``tns``, SOAP is based on XML, so no wonder we need a root namespace.
#. ``location``, it tells our server, where it lives. It is only a piece of
   information required by pyws to generate a proper WSDL description, the real
   binding to URL will appear later.

Now it's time to introduce our first function. To register it we need to wrap
it up with a special decorator, so it will look like this::

    from pyws.functions.register import register

    @register
    def add_simple(a, b):
        return a + b

And the last step, we need to edit ``urls.py``, the result would be as
following::

    from django.conf.urls.defaults import *
    from pyws.adapters._django import serve
    from pywstest.server import server

    urlpatterns = patterns('',
        url('^api/(.*)', serve, {'server': server})
    )

Here we binded our server to a real URL. Function ``serve`` is an adapter used
to convert Django requests/responses to/from pyws requests/responses.

That's it! Let's test it.


Results
-------

First, start a server::

    $ python ./manage.py runserver

Prepare a request::

    $ cat > request
    <?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <add_simple xmlns="http://www.example.org/">
          <a>hello </a>
          <b>world</b>
        </add_simple>
      </soap:Body>
    </soap:Envelope>

Then hit it::

    $ curl --data-binary @request http://localhost:8000/api/

The result would be::

    <?xml version='1.0' encoding='utf-8'?>
    <se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
      <se:Body>
        <add_simple_response namespace="http://example.com/">
          <result>hello world</result>
        </add_simple_response>
      </se:Body>
    </se:Envelope>

Hey, it looks like we've just concatenated two strings via SOAP.
Congratulations!

Next, we are going to introduce WSDL and use a SOAP client to send requests,
follow :doc:`me <getting_started_part_2>`.
