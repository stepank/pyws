import logging
import traceback

from errors import Error, BadProtocol, FunctionNotFound, ProtocolError, \
    ProtocolNotFound, ET_CLIENT, ET_SERVER
from protocols import Protocol
from response import Response


class Server(object):

    def __init__(self, settings):
        self.settings = settings

    @property
    def location(self):
        return self.settings.LOCATION

    def get_protocol(self, request):

        parts = request.tail.split('/', 1)

        name, tail = parts[0], (len(parts) > 1 and parts[1] or '')

        request.tail = tail

        protocol = self.settings.PROTOCOLS.get(name)

        if not protocol:
            raise ProtocolNotFound(name)

        if isinstance(protocol, Protocol):
            return protocol

        if isinstance(protocol, type) and issubclass(protocol, Protocol):
            return protocol()

        if isinstance(protocol, dict):
            try:
                cls = protocol['class']
                args = protocol['args']
                kwargs = protocol['kwargs']
            except KeyError:
                raise BadProtocol(protocol)
            return cls(*args, **kwargs)

        raise BadProtocol(protocol)

    def get_function(self, name, quiet=False):
        for manager in self.settings.FUNCTION_MANAGERS:
            try:
                return manager.get_one(name)
            except FunctionNotFound:
                pass
        if quiet:
            return None
        raise FunctionNotFound(name)

    def get_functions(self):
        return reduce(lambda x, y: x + y,
            (manager.get_all() for manager in self.settings.FUNCTION_MANAGERS))

    def can_authenticate(self):
        return hasattr(self.settings, 'AUTHENTICATOR')

    def authenticate(self, protocol, request):
        data = protocol.get_auth_data(request)
        self.settings.AUTHENTICATOR(data)

    def process_request(self, request):

        logging.debug(request)

        try:
            protocol = self.get_protocol(request)
        except ProtocolError, e:
            return Response(unicode(e))

        try:

            function = protocol.get_function(request)

            if callable(function):
                return function(self, request)

            if isinstance(function, tuple):
                name, args = function
            else:
                name, args = function, None

            can_authenticate = self.can_authenticate()
            function = self.get_function(name, quiet=can_authenticate)
            if can_authenticate and (not function or function.needs_auth):
                self.authenticate(protocol, request)
                if not function:
                    function = self.get_function(name)

            if args is None:
                args = protocol.get_arguments(request, function.args)

            result = function(**args)

            response = protocol.get_response(
                result, name, function.return_type)

        except Error, e:
            logging.error(traceback.format_exc())
            response = protocol.get_error_response(e)
        except Exception, e:
            logging.error(traceback.format_exc())
            client_error = hasattr(e, '__module__') or type(e) == Exception
            if not client_error and self.settings.DEBUG:
                raise
            e.error_type = client_error and ET_CLIENT or ET_SERVER
            response = protocol.get_error_response(e)

        logging.debug(response)

        return response
