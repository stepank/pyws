from args import Field, Dict, DictOf, String, Type


class Function(object):

    def __init__(self, name, return_type=None, args=None, needs_auth=False):
        self.name = name
        self.return_type = return_type or String
        self.args = DictOf(name.capitalize() + 'Function', *args)
        self.needs_auth = needs_auth

    def __call__(self, **args):
        args = self.validate(args)
        return self.call(**args)

    def validate(self, args):
        return self.args.validate(args)

    def call(self, **args):
        raise NotImplementedError('Function.call')


class NativeFunctionAdapter(Function):

    def __init__(self, 
            origin, name=None, return_type=None, args=None, *nargs, **kwargs):
        self.origin = origin
        arg_names = map(lambda x: (x, ), self.origin.func_code.co_varnames)
        if not args:
            args = (String, ) * len(arg_names)
        args_ = map(lambda x: x[0] + x[1], zip(arg_names, map(lambda arg:
            isinstance(arg, (tuple, list)) and arg or (arg, ), args)))
        super(NativeFunctionAdapter, self). \
            __init__(name=name or origin.__name__,
                return_type=return_type, args=args_, *nargs, **kwargs)

    def call(self, **args):
        return self.origin(**args)
