try:
    import json
except ImportError:
    #noinspection PyUnresolvedReferences
    import simplejson as json

from functools import partial

from pyws.errors import BadRequest
from pyws.response import Response

from base import Protocol

__all__ = ('RestProtocol', 'JsonProtocol', )

create_response = partial(Response, content_type='application/json')
create_error_response = partial(create_response, status=Response.STATUS_ERROR)


class RestProtocol(Protocol):

    name = 'rest'

    def get_function(self, request):
        return request.tail

    def get_arguments(self, request, arguments):
        return dict((k, len(v) > 1 and v or v[0])
            for k, v in request.GET.iteritems())

    def get_response(self, result, name, return_type):
        return create_response(json.dumps({'result': result}))

    def get_error_response(self, error):
        return create_error_response(
            json.dumps({'error': self.get_error(error)}))


class JsonProtocol(RestProtocol):

    name = 'json'

    def get_arguments(self, request, arguments):
        try:
            return json.loads(request.text)
        except ValueError:
            raise BadRequest()
