from pyws.functions import NativeFunctionAdapter
from pyws.server import SERVERS


class Register(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, origin=None, *args, **kwargs):

        if args or kwargs or not callable(origin):
            if not callable(origin):
                args = (origin, ) + args
                origin = None
            register = Register(*args, **kwargs)
            return origin and register(origin) or register

        try:
            server = SERVERS[self.kwargs.pop('to')]
        except KeyError:
            server = SERVERS.default

        server.add_function(
            NativeFunctionAdapter(origin, *self.args, **self.kwargs))

        return origin


register = Register()
