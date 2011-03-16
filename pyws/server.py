from errors import Error, BadProtocol, ProtocolError, ProtocolNotFound
from functions.managers import FunctionNotFound
from protocols import Protocol
from response import Response


class Server(object):

    def __init__(self, settings):
        self.settings = settings

    def get_protocol(self, request):

        parts = request.tail.split('/', 1)

        name, tail = parts[0], (len(parts) > 1 and parts[1] or '')

        request.tail = tail

        info = self.settings.PROTOCOLS.get(name)

        if not info:
            raise ProtocolNotFound(name)

        if isinstance(info, Protocol):
            return info

        if isinstance(info, type) and issubclass(info, Protocol):
            return info()

        if isinstance(info, dict):
            try:
                cls = info['class']
                args = info['args']
                kwargs = info['kwargs']
            except KeyError:
                raise BadProtocol(info)
            return cls(*args, **kwargs)

        raise BadProtocol(info)

    def get_function(self, name):
        for manager in self.settings.FUNCTION_MANAGERS:
            try:
                return manager.get_one(name)
            except FunctionNotFound:
                pass
        raise FunctionNotFound(name)

    def process_request(self, request):

        try:
            protocol = self.get_protocol(request)
        except ProtocolError, e:
            return Response(unicode(e))

        try:

            function = protocol.get_function(request)

            if callable(function):
                return function(request)

            name, args = function
            function = self.get_function(name)
            result = function(**args)

            return protocol.get_response(result)

        except Error, e:

            return protocol.get_error_response(e)