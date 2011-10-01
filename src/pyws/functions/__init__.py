from args import DictOf, TypeFactory

CONTEXT_ARG_NAME = 'context'


class Function(object):

    def __init__(self, name, return_type=None, args=None, needs_context=False):
        self.name = name
        self.return_type = TypeFactory(return_type or str)
        self.args = DictOf(name.capitalize() + 'Function', *args)
        self.needs_context = needs_context

    def __call__(self, context, **args):
        args = self.validate(args)
        if self.needs_context:
            args[CONTEXT_ARG_NAME] = context
        return self.call(**args)

    def validate(self, args):
        return self.args.validate(args)

    def call(self, **args):
        raise NotImplementedError('Function.call')


class NativeFunctionAdapter(Function):

    def __init__(
            self, origin,
            name=None, return_type=None, args=None, needs_context=False):

        self.origin = origin

        arg_names = [(x, ) for x in self.origin.func_code.co_varnames
            if not needs_context or x != CONTEXT_ARG_NAME]

        if not args:
            args = (str,) * len(arg_names)
        args_ = map(lambda x: x[0] + x[1], zip(arg_names,
            map(lambda arg: isinstance(arg, tuple) and arg or (arg,), args)))

        super(NativeFunctionAdapter, self).__init__(
            name=name or origin.__name__, return_type=return_type,
            args=args_, needs_context=needs_context)

    def call(self, **args):
        return self.origin(**args)
