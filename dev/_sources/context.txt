.. _context:

Context
=======

A result returning by a function can depend not only on the argument values,
but also on the context which the function is running in. So we need a
mechanism to work with the context.

In pyws this mechanism consists of the following parts:

* A protocol can extract context data from a request.

    As described in chapter :ref:`protocol_implementation` a protocol has two
    context data getters which extract context data for different cases.

* A server can create a context from these data.

    To create a context a server calls a function ``CREATE_CONTEXT`` specified
    in the server settings. This function accepts exactly one argument, namely
    context data extracted from a request, creates and returns the context. If
    an exception is raised and a function requires the context, the server will
    stop processing the request and report an error.

* A function can require and use the context.

    If the function was returned directly by a protocol it accepts exactly
    three arguments: a server object, a request object and and a context.
    Otherwise, it called with the is the function requires a context it is
    passed as ``context`` keyword argument.

* A server can destroy the context.

    To destroy the context a server calls a function ``DESTROY_CONTEXT``
    specified in the server settings. This function accepts exactly one
    argument, namely the context, it cleans it, if it is necessary.


.. _authentication:

Authentcation
-------------

All the stuff described above can be easily used to handle authentication in
an API.

For instance, if we use :ref:`SOAP protocol <soap_protocol>`, we can
instantiate it with the following ``headers_schema``:

.. literalinclude:: ../examples/authenticate.py
    :lines: 3-7

Then we can define a function creating a context that will check a username
and a password. If the protocol is able to extract context data according to
this schema, the function will receive a dict
``{'username': '...', 'password': '...'}`` as its only argument:

.. literalinclude:: ../examples/authenticate.py
    :lines: 9-12

This function returns a username, that will be passed as ``context`` keyword
argument to functions, that need a context. If you are working in thread safe
environment, for instance, one thread per each request, you can store the
context in thread local variables. In this case the function might just return
``None``.

If a function creating a context raises an exception, it's ok, unless the
function being called does not need a context, otherwise pyws will report an
error.
