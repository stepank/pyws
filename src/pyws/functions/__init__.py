#noinspection PyUnresolvedReferences
from pyws.functions.args import DictOf, TypeFactory
from pyws.utils import cached_property

__all__ = ('Function', 'NativeFunctionAdapter', )

CONTEXT_ARG_NAME = 'context'


class Function(object):
    """
    An abstract function class. Implements simple context handling and argument
    values validation.
    """

    #: the name of the function;
    name = None
    #: the documentation of the function
    documentation = None
    #: the type of values returning by the function (standard form only), see
    #: :ref:`type_specification`;
    return_type = None
    #: function arguments specification, a ``pyws.functions.args.Dict`` type
    #: (standard form only) with arguments as fields, see
    #: :ref:`arguments_specification` and :ref:`type_specification`;
    args = None
    #: shows whether the function requires a context to run.
    needs_context = False

    def __call__(self, context, **args):
        """
        Validates argument values and checks if the function requires a
        context. If it does, argument ``context`` is added to other arguments
        and method ``call`` is called.
        """
        args = self.validate(args)
        if self.needs_context:
            if isinstance(context, Exception):
                raise context
            args[CONTEXT_ARG_NAME] = context
        return self.call(**args)

    @cached_property
    def type_name(self):
        return self.name

    @cached_property
    def wrapped_return_type(self):
        return args.DictOf(
            self.type_name + '_result', args.Field('result', self.return_type))

    def validate(self, args):
        return self.args.validate(args)

    def call(self, **args):
        """
        This method must implement the logic of the function. ``args`` is a
        dict of validated argument values including key ``context`` if it is
        required.
        """
        raise NotImplementedError('Function.call')


class NativeFunctionAdapter(Function):
    """
    This class allows to wrap any native python function so that it behaved
    like ``pyws.functions.Function``.
    """

    def __init__(
            self, origin,
            name=None, return_type=str, args=None, needs_context=False):
        """
        ``origin`` is a native Python function to be wrapped.
        ``name`` is the name of the function, if it is not specified,
        ``origin.__name__`` is used. ``return_type`` and ``needs_context``
        correspond to ``pyws.functions.Function`` arguments. ``args`` is a
        tuple, each of its elements may be:

        * a type,
        * a tuple, first element is a type, second is a value representing an
          empty one.

        If ``args`` is not specified all arguments will be treated as strings,
        the same thing with ``return_type``. Argument names are infered from
        ``origin.func_code.co_varnames``.

        >>> from pyws.functions import NativeFunctionAdapter
        >>> from pyws.functions.args import String
        >>> from pyws.functions.args import Dict, Field

        >>> def nothing():
        ...     pass

        >>> a = NativeFunctionAdapter(nothing)
        >>> a.origin == nothing
        True
        >>> a.name
        'nothing'
        >>> a.return_type
        <class 'pyws.functions.args.types.simple.String'>
        >>> issubclass(a.args, Dict)
        True
        >>> a.args.fields
        []
        >>> a(context=None)

        >>> def add(a, b):
        ...     return a + b

        >>> a = NativeFunctionAdapter(add, name='concat')
        >>> a.name
        'concat'
        >>> len(a.args.fields)
        2
        >>> f = a.args.fields[0]
        >>> type(f)
        <class 'pyws.functions.args.field.Field'>
        >>> f.name
        'a'
        >>> f.type
        <class 'pyws.functions.args.types.simple.String'>
        >>> a.return_type
        <class 'pyws.functions.args.types.simple.String'>

        >>> a = NativeFunctionAdapter(
        ...     add,
        ...     name='sum',
        ...     return_type=int,
        ...     args=(int,),
        ... )
        >>> a.name
        'sum'
        >>> f = a.args.fields[0]
        >>> f.type
        <class 'pyws.functions.args.types.simple.Integer'>
        >>> a.return_type
        <class 'pyws.functions.args.types.simple.Integer'>

        >>> def empty_value(a):
        ...     return 'hello ' + a

        >>> a = NativeFunctionAdapter(empty_value, args=((str, 'world'), ))
        >>> a(context=None, a=None) # note that 'world' is used instead of None
        'hello world'
        """

        self.origin = origin

        self.name = name or origin.__name__
        self.documentation = origin.__doc__
        self.return_type = TypeFactory(return_type or str)
        self.needs_context = needs_context

        # Get argument names from origin
        arg_names = [(x, ) for x in self.origin.func_code.co_varnames
            if not needs_context or x != CONTEXT_ARG_NAME]

        # Get argument types
        if not args:
            args = (str,) * len(arg_names)
        args_ = map(lambda x: x[0] + x[1], zip(arg_names,
            map(lambda arg: isinstance(arg, tuple) and arg or (arg,), args)))

        # Build arguments specification
        self.args = DictOf(self.type_name, *args_)

    def call(self, **args):
        """
        Simply calls origin function with ``args`` argument values.
        """
        return self.origin(**args)
