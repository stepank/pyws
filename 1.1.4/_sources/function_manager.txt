.. _function_manager:

Function manager
================

Having a fixed set of functions in an API might be inapplicable in some cases,
that's why there is a concept of function managers in pyws. When a server tries
to determine a function to call it asks each of its function managers whether
it has one. Also, for instance, when WSDL description is generated, a server
needs to know full list of its functions, function managers help
with this task too.

.. autoclass:: pyws.functions.managers.FunctionManager
   :members: get_one,get_all


Fixed function manager
----------------------

pyws has only one predefined function manager, namely a fixed one.

.. autoclass:: pyws.functions.managers.FixedFunctionManager
   :members: __init__,add_function,get_one,get_all

Each pyws server has a fixed function manager preinstalled, however there is no
restriction on how many and what function managers a server might have.


.. _registering_function:

Registering a function
----------------------

If you have a ``pyws.functions.Function`` object, you can register it to a
server using its method ``add_function``:

.. automethod:: pyws.server.Server.add_function

However, if you have an ordinary python function, there is an easier way, just
use function ``pyws.functions.register.register``:

.. autofunction:: pyws.functions.register.register
