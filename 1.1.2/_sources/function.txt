.. _function:

Function
========

To implement a function, you need to inherit its class from class
``pyws.functions.Function`` and implement its method ``call``, also it must
have attributes ``name``, ``return_type`` and ``args``. To call a function, a
server just calls it as any callable object, so there is a default
implemenetation of method ``__call__``:

.. autoclass:: pyws.functions.Function
   :members: name,return_type,args,needs_context,__call__,call


Native function adapter
-----------------------

However, there is an easier way to implement a function, namely using
``pyws.functions.NativeFunctionAdapter`` class:

.. autoclass:: pyws.functions.NativeFunctionAdapter
   :members: __init__,call


.. _arguments_specification:

Arguments & fields specification
--------------------------------

One of the main differences between python and WSDL is that the former uses
duck typing, whereas the latter requires strict types specification, therefore
we need to be able to specify types. In most cases, when you need to specify an
argument or a field, you can do it in two forms:

* standard, a ``Field`` object,
* simplified, a tuple of arguments for a ``Field`` object.

.. autoclass:: pyws.functions.args.field.Field
   :members: __init__


.. _type_specification:

Type specification
------------------

In pyws in all cases, when you need to specify a type, you can do it in two
forms:

* standard, using one of ``pyws.functions.args.types.base.Type`` successors,
* simplified, using python built-in types,

pyws supports the following types:

.. automodule:: pyws.functions.args.types
   :members: String,Integer,Float,Date,DateTime,Dict,List

Three helper functions are also at your disposal:

.. autofunction:: pyws.functions.args.DictOf
.. autofunction:: pyws.functions.args.ListOf
.. autofunction:: pyws.functions.args.TypeFactory
