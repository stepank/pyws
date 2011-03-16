from args import Field, Record, String

def getter(name):
    def wrapped(self):
        attr = getattr(self, name)
        if callable(attr):
            return attr()
        return attr
    return wrapped


class FunctionInfo(object):

    def __init__(self, return_type, args):
        self.return_type = return_type
        self.args = args


class Function(object):

    def __call__(self, **args):

        args = self.validate(args)

        return self.call(**args)

    name = property(getter('_name'))
    info = property(getter('_info'))

    def validate(self, args):
        return self.info.args.validate(args)

    def call(self, **args):
        raise NotImplemented('Function.call')


class SimpleFunctionAdapter(Function):

    def __init__(self, origin):
        self.origin = origin

    def call(self, **args):
        return self.origin(**args)

    def _name(self):
        return self.origin.__name__

    def _info(self):
        return FunctionInfo(String, Record(self.name.capitalize() + 'Function',
            *(Field(name, String) for name in self.origin.func_code.co_varnames)))
