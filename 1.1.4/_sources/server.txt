.. _server:

Server
======

The central node of pyws infrastructure is a server, it is defined in module
``pyws.server``. There are two classes defined: ``Server`` (a generic server)
and ``SoapServer``. There is only one difference between them, namely the
latter has a SOAP protocol registered beforehand.

The easiest way to create a generic server is this::

    from pyws.server import Server
    server = Server(settings)

To create a SOAP server::

    from pyws.server import SoapServer
    server = SoapServer(
        settings,
        service_name='Test',
        tns='http://example.com/',
        location='http://localhost:8000/api/',
    )

In both cases ``settings`` may be a dict or an object (a module object as well)
containing some, well, settings. Other parameters in the case of a SOAP server
are:

#. ``service_name`` gives a name to the server, it is used to generate WSDL
   description.
#. ``tns`` is a root namespace, where all the stuff lives. SOAP is based on
   XML, so no wonder we need it.
#. ``location`` tells the server, where it lives. It is only a piece of
   information required by pyws to generate a proper WSDL description, it is
   not a real binding to an URL.


Settings
--------

A server has the following settings variables.

NAME
^^^^

``NAME`` is used to identify a pyws server. For example, if you have several
pyws servers, you have to specify a server name to register a function to it.
Server name is unique, thus creating two servers with the same name raises an
exception. Default is ``None``.

.. _settings_debug:

DEBUG
^^^^^

If ``DEBUG`` is ``True`` a server will not catch exceptions occuring in
registered functions, but rather it will just pass them further so that you
could handle them your own way. For example, Django in debug mode will print a
pretty formatted stack trace. Default is ``False``.

.. _settings_protocols:

PROTOCOLS
^^^^^^^^^

A tuple of :doc:`protocol <protocol>` instances that a server will use to
process requests. For ``SoapServer`` default is a tuple of a single SOAP
protocol instance. For a generic ``Server`` there are no protocol predefined,
so make sure you've register at least one yourself.

FUNCTION_MANAGERS
^^^^^^^^^^^^^^^^^

A tuple of :ref:`function managers <function_manager>` that provide a server
with functions. Default is a tuple of a single fixed function manager.

.. _settings_create_context:

CREATE_CONTEXT
^^^^^^^^^^^^^^

A function creating a context for request processing. Default is ``None``. More
about context handling read in chapter :doc:`context`.

DESTROY_CONTEXT
^^^^^^^^^^^^^^^

A function destroying a previously defined context. Default is ``None``. More
about context handling read in chapter :doc:`context`.
