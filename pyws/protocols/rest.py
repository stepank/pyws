import json

from pyws.errors import BadRequest
from pyws.response import Response

from base import Protocol

__all__ = ('RestProtocol', 'JsonProtocol', )


class RestProtocol(Protocol):

    def get_function(self, request):
        return (request.tail,
            dict((k, len(v) > 1 and v or v[0])
                for k, v in request.GET.iteritems()))

    def get_response(self, result, name, return_type):
        return Response(json.dumps({'result': result}))

    def get_error_response(self, error):
        return Response(json.dumps({'error': self.get_error(error)}))


class JsonProtocol(RestProtocol):

    def get_function(self, request):
        try:
            args = json.loads(request.text)
        except ValueError:
            raise BadRequest()
        return request.tail, args
