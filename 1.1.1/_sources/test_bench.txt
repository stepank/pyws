.. _test_bench:

Test bench
==========

SOAP server can not be considered a good one if SOAP clients don't work with
it. Therefore we need a lot of tests proving interoperability. This chapter
describes a test bench used by numerous tests proving interoperability included
in pyws. The next chapter :ref:`running_tests` explains how to run a server and
all the tests. All of this can also be considered examples of pyws usage since
much of pyws's functionality is used here.

To proceed with the tests, first, ensure that pyws is installed, read more
about :ref:`requirements` and :ref:`installation`, this tutorial is based on
WSGI adapter, so check up its requirements too. You should also note that tests
and examples can be found only in a source distribution archive or in your own
clone of the GIT repo.


Directory structure
-------------------

In pyws distribution, there is a directory called ``examples``, let's have a
look at its contents::

    examples/
        _django/                # not for now ...
        _twisted/               # not for now either ...
        _wsgi/
            __init__.py         # a simple WSGI application for testing
            Makefile            # a make file to automate running and stopping
                                # a server
        __init__.py
        api_settings.py         # common pyws server settings
        authenticate.py         # authentication related stuff
        functions.py            # example functions
        server.py               # server definition


Server & settings
-----------------

First, let's consider ``server.py``:

.. literalinclude:: ../examples/server.py
    :lines: 3-4,6

Here we create a server using class ``SoapServer`` with module object
``api_settings`` as settings and with ``api_settings.SOAP_PROTOCOL_PARAMS``
as SOAP protocol parameters.

Now, let's turn to ``api_settings.py``:

.. literalinclude:: ../examples/api_settings.py
    :lines: 5

That's easy, turns debug mode on, read more in :ref:`settings_debug`.

.. literalinclude:: ../examples/api_settings.py
    :lines: 7-10

Additional protocols for the server, read more in :ref:`settings_protocols`.

.. literalinclude:: ../examples/api_settings.py
    :lines: 12-17

These parameters are passed directly to SOAP protocol constructor, read more in
:ref:`soap_protocol`.

.. literalinclude:: ../examples/api_settings.py
    :lines: 19

The function creating a context , read more in :ref:`settings_create_context`.


Authentication
--------------

In the previous paragraph, there were mentioned two variables:
``soap_headers_schema`` and ``authenticate``, they are defined in
``authenticate.py``, read more in :ref:`authentication`.


Functions
---------

All the functions used in tests are defined in file ``functions.py``. They
are an example of how functions can be registered to a server and how their
parameters are described, so you might want to cast a glance at it. Most use
cases are described in this paragraph, but the file contains a little bit more
examples.


Simple examples
^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 4-5,9-13

Decorators created by function ``register`` only register a function to a
server without changing it at all, so we can safely use several decorators at
once. As one function can work with different types of variables we can
register one function with different names and argument specification.

``args`` describes function arguments, each element of the tuple represents
one argument, argument names are infered from the function. ``(int, 0)`` means
that an argument has type ``int`` and that instead of ``None`` you'll get
``0``. We could have just use ``int`` instead, but then we had to check
argument values on not being ``None`` in function itself, which might not be
convenient.

The first decorator ``register()`` will register a function with its own name
and all arguments and return values will be treated as strings.

Read more in chapters :ref:`registering_function`,
:ref:`arguments_specification`, :ref:`type_specification`.


Context example
^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 18-20

This function requires a context, so we register it specifying
``needs_context`` as ``True``. If a server fails to create a context, then this
function is not called and an exception is raised instead. The context created
by a server is passed to the function as keyword argument ``context``.

Read more in chapter :ref:`context`.


Date and datetime example
^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 25-35

Well, it looks pretty straight forward.

Read more in chapters :ref:`arguments_specification`,
:ref:`type_specification`.


Dict example
^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 41

Value with key ``0`` is the name of a dictionary type, other keys and values
represent field names and their types.

.. literalinclude:: ../examples/functions.py
    :lines: 44

Callables can be used as none values.

.. literalinclude:: ../examples/functions.py
    :lines: 54-66


List examples
^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 71-83

List type definition is pretty simple, isn't it?

.. literalinclude:: ../examples/functions.py
    :lines: 85-97

``IntegerList``'s second element is an element none value.


Recursive type example
^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 102-114

So far, the only way to create a recursive type is monkey pathcing.


Exception raising example
^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/functions.py
    :lines: 133-142

It's easy, just raise any exception you want.
