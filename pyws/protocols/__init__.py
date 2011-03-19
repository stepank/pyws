import json

from pyws.errors import ET_CLIENT
from pyws.response import Response


class Protocol(object):

    def __init__(self, *args, **kwargs):
        pass

    def get_function(self, request):
        raise NotImplemented('Protocol.get_function')

    def get_response(self):
        raise NotImplemented('Protocol.get_response')

    def get_error(self, error):
        error_type = type(error)
        if error.error_type == ET_CLIENT:
            error_type_name = 'Client'
        else:
            error_type_name = 'Server'
        return {
            'error': {
                'type': error_type_name,
                'name': error_type.__name__,
                'prefix': error_type.__module__,
                'message': unicode(error),
                'params': error.args,
            }
        }


class SoapProtocol(Protocol):

    def get_function(self, request):

        if request.tail == 'wsdl':
            return self.get_wsdl

        return 'simple', {'s': 'hello'}

    def get_wsdl(self, request):
        return Response('wsdl')


class RestProtocol(Protocol):

    def get_function(self, request):
        return (request.tail,
            dict((k, len(v) > 1 and v or v[0])
                for k, v in request.GET.iteritems()))

    def get_response(self, result):
        return Response(json.dumps({'result': result}))

    def get_error_response(self, error):
        return Response(json.dumps(self.get_error(error)))
