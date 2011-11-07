Protocol
========

Basically, a protocol performs the following tasks:

* extracts a function name and argument values from a request,
* extracts context data from the request,
* forms a response out of the result returned by the function,
* forms an error response in the case of an exception.

When a server asks a protocol to extract a function name the protocol may
return either a function name or a callable object.

In the former case, the server will request argument values after determining
the function and its arguments specification.

In the latter case, the callable object is directly called with three
arguments: a server object, a request object and and a context. This is used
for special cases, currently only for WSDL descrption generation.


.. _protocol_implementation:

Protocol implementation
-----------------------

A protocol must be an instance of ``pyws.protocols.base.Protocol`` and must
implement methods ``get_function``, ``get_arguments``, ``get_response``,
``get_error_response``.

.. autoclass:: pyws.protocols.base.Protocol
   :members: __init__,get_function,get_arguments,get_response,
             get_error_response,get_error


.. _soap_protocol:

Concerning SOAP protocol
------------------------

SOAP can't be thought of without WSDL, so to instantiate this protocol we need
some information. Also for SOAP, the usual practice is to specify a context in
SOAP envelope headers, so a simple context data getter is implemented for your
convenience. The only thing you need to do to implement context data extraction
from a request is to specify headers schema:

.. automethod:: pyws.protocols.soap.SoapProtocol.__init__
