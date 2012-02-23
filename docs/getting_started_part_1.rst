Getting started, part 1
=======================

In this tutorial we are going to install pyws SOAP server providing WSDL,
add there some functions and test it.


Environment
-----------

Ensure that pyws is installed, read more about :ref:`requirements` and
:ref:`installation`, this tutorial is based on Django adapter, so check up its
requirements too. Also you will need curl for testing purposes.


Project
-------

Let's create a new Django project::

    $ django-admin.py startproject pywstest
    $ cd !$

If you have problems with this refer to
`Django documentation <https://docs.djangoproject.com/en/1.3/intro/tutorial01/#creating-a-project>`_.

Here we will create a file ``server.py``, which we are going to edit::

    $ touch server.py


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

    @register()
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

    $ python manage.py runserver

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
        <add_simple_result namespace="http://example.com/types/">
          <result>hello world</result>
        </add_simple_result>
      </se:Body>
    </se:Envelope>

Hey, it looks like we've just concatenated two strings via SOAP.
Congratulations!

Next, we are going to introduce WSDL and use a SOAP client to send requests,
follow :doc:`me <getting_started_part_2>`.
