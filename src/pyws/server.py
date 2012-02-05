from __future__ import with_statement

import logging
import traceback

from pyws.errors import Error, BadProtocol, FunctionNotFound, ProtocolError, \
    ProtocolNotFound, ET_CLIENT, ET_SERVER, ServerAlreadyRegistered, \
    ConfigurationError, NoProtocolsRegistered, DefaultServerAlreadyRegistered
from pyws.functions.managers import FixedFunctionManager
from pyws.protocols import Protocol, SoapProtocol
from pyws.response import Response
from pyws.settings import Settings

logger = logging.getLogger('pyws')


class ServersDict(dict):
    default = None


SERVERS = ServersDict()


class ContextManager(object):

    def __init__(self, context_data, enter, exit):
        self.context_data = context_data
        self.enter = enter
        self.exit = exit

    def __enter__(self):
        try:
            self.context = self.enter(self.context_data)
        except Exception, e:
            self.context = e
        return self.context

    #noinspection PyUnusedLocal
    def __exit__(self, *args, **kwargs):
        self.exit(self.context)


class Server(object):

    def defaults(self):
        return dict(
            NAME=None,
            DEBUG=False,
            DEFAULT=False,
            FUNCTION_MANAGERS=(FixedFunctionManager(), ),
            CREATE_CONTEXT=lambda x: None,
            DESTROY_CONTEXT=lambda x: None,
        )

    def __init__(self, settings=None):
        if not settings:
            settings = {}
        self.settings = self.gather_settings()
        self.settings.update(settings)
        if self.name in SERVERS:
            raise ServerAlreadyRegistered(self.name)
        SERVERS[self.name] = self
        if not SERVERS.default or self.settings.DEFAULT:
            if self.settings.DEFAULT and \
                    SERVERS.default and SERVERS.default.settings.DEFAULT:
                raise DefaultServerAlreadyRegistered()
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

        if not isinstance(protocol, Protocol):
            raise BadProtocol(protocol)

        return protocol

    def add_function(self, function):
        """
        Registers the function to the server's default fixed function manager.
        """
        #noinspection PyTypeChecker
        if not len(self.settings.FUNCTION_MANAGERS):
            raise ConfigurationError(
                'Where have default function manager gone?!')
        #noinspection PyUnresolvedReferences
        self.settings.FUNCTION_MANAGERS[0].add_function(function)

    def get_function(self, context, name):
        for manager in self.settings.FUNCTION_MANAGERS:
            try:
                return manager.get_one(context, name)
            except FunctionNotFound:
                pass
        raise FunctionNotFound(name)

    def get_functions(self, context):
        return reduce(
            lambda x, y: x + y,
            (manager.get_all(context)
                for manager in self.settings.FUNCTION_MANAGERS)
        )

    def get_context_manager(self, context_data):
        return ContextManager(
            context_data,
            getattr(self.settings, 'CREATE_CONTEXT', lambda a: None),
            getattr(self.settings, 'DESTROY_CONTEXT', lambda a: None)
        )

    def process_request(self, request):

        logger.debug(request)

        try:
            protocol = self.get_protocol(request)
        except ProtocolError, e:
            return Response(unicode(e))

        try:

            function = protocol.get_function(request)

            if not callable(function):
                context_data = protocol.get_context_data(request)
            else:
                context_data = protocol.get_common_context_data(request)

            with self.get_context_manager(context_data) as context:

                if callable(function):
                    return function(self, request, context)

                function = self.get_function(context, function)

                args = protocol.get_arguments(request, function.args)

                result = function(context, **args)

            response = protocol.get_response(
                result, function.name, function.return_type)

        except Error, e:
            logger.error(traceback.format_exc())
            response = protocol.get_error_response(e)
        except Exception, e:
            logger.error(traceback.format_exc())
            client_error = hasattr(e, '__module__') or type(e) == Exception
            if not client_error and self.settings.DEBUG:
                raise
            e.error_type = client_error and ET_CLIENT or ET_SERVER
            response = protocol.get_error_response(e)

        logger.debug(response)

        return response


class SoapServer(Server):

    def defaults(self):
        return Settings(
            PROTOCOLS=(self.soap_protocol, )
        )

    def __init__(self, settings=None, *args, **kwargs):
        self.soap_protocol = SoapProtocol(*args, **kwargs)
        super(SoapServer, self).__init__(settings)
