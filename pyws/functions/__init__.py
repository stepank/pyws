from args import Field, Dict, String


class Function(object):

    def __init__(self, name, return_type=None, args=None):
        self.name = name
        self.return_type = return_type or String
        if isinstance(args, Dict):
            self.args = args
        else:
            self.args = Dict(name.capitalize() + 'Function',
                *(Field(*field_args) for field_args in args))

    def __call__(self, **args):
        args = self.validate(args)
        return self.call(**args)

    def validate(self, args):
        return self.args.validate(args)

    def call(self, **args):
        raise NotImplemented('Function.call')


class SimpleFunctionAdapter(Function):

    def __init__(self, origin, name=None, return_type=None, args=None):
        self.origin = origin
        super(SimpleFunctionAdapter, self).__init__(
            name=name or origin.__name__,
            return_type=return_type,
            args=args or ((name, String) for name in self.origin.func_code.co_varnames)
        )

    def call(self, **args):
        return self.origin(**args)
