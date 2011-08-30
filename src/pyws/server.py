import logging
import traceback

from pyws.errors import Error, BadProtocol, FunctionNotFound, ProtocolError, \
    ProtocolNotFound, ET_CLIENT, ET_SERVER, ServerAlreadyRegistered, \
    ConfigurationError, NoProtocolsRegistered
from pyws.functions.managers import FixedFunctionManager
from pyws.protocols import Protocol, SoapProtocol
from pyws.response import Response
from pyws.settings import Settings


class ServersDict(dict):
    default = None


SERVERS = ServersDict()


class Server(object):

    def defaults(self):
        return dict(
            NAME=None,
            DEBUG=False,
            FUNCTION_MANAGERS=(FixedFunctionManager(), ),
        )

    def __init__(self, settings=None):
        if not settings:
            settings = {}
        self.settings = self.gather_settings()
        self.settings.update(settings)
        if self.name in SERVERS:
            raise ServerAlreadyRegistered(self.name)
        SERVERS[self.name] = self
        SERVERS.default = self

    def gather_settings(self, result=None, cls=None):
        if not result:
            result = Settings()
        if not cls:
            cls = type(self)
        if not hasattr(cls, 'defaults'):
            return Settings()
        result = reduce(self.gather_settings, cls.__bases__, result)
        #noinspection PyUnresolvedReferences
        result.update(
            callable(cls.defaults) and cls.defaults(self) or cls.defaults)
        return result

    @property
    def name(self):
        return self.settings.NAME

    @property
    def protocols(self):
        if not hasattr(self, '_protocols'):
            self._protocols = dict(
                (protocol.name, protocol)
                    for protocol in self.settings.PROTOCOLS)
        return self._protocols

    def get_protocol(self, request):

        if not self.protocols:
            raise NoProtocolsRegistered()

        if len(self.protocols) == 1:
            name, tail = self.protocols.keys()[0], request.tail
        else:
            parts = request.tail.split('/', 1)
            name, tail = parts[0], (len(parts) > 1 and parts[1] or '')
            request.tail = tail

        protocol = self.protocols.get(name)

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

    def add_function(self, function):
        if not len(self.settings.FUNCTION_MANAGERS):
            raise ConfigurationError(
                'Where have default function manager gone?!')
        self.settings.FUNCTION_MANAGERS[0].add_function(function)

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
        #noinspection PyCallingNonCallable
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


class SoapServer(Server):

    def defaults(self):
        return Settings(
            PROTOCOLS=(self.soap_protocol, )
        )

    def __init__(self, settings=None, *args, **kwargs):
        self.soap_protocol = SoapProtocol(*args, **kwargs)
        super(SoapServer, self).__init__(settings)
