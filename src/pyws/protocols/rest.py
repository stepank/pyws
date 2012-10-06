from datetime import date, datetime

from functools import partial

from pyws.errors import BadRequest
from pyws.functions.args.types.complex import List
from pyws.response import Response
from pyws.utils import json
from pyws.protocols.base import Protocol

__all__ = ('RestProtocol', 'JsonProtocol', )


class DateIso8601Encoder(json.JSONEncoder):
    # JSON Serializer with datetime support
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


create_response = partial(Response, content_type='application/json')
create_error_response = partial(create_response, status=Response.STATUS_ERROR)


class RestProtocol(Protocol):

    name = 'rest'

    def get_function(self, request):
        return request.tail

    def get_arguments(self, request, arguments):
        result = {}
        for field in arguments.fields:
            value = request.GET.get(field.name)
            if issubclass(field.type, List):
                result[field.name] = value
            elif field.name in request.GET:
                result[field.name] = value[0]
        return result

    def get_response(self, result, name, return_type):
        return create_response(
            json.dumps({'result': result}, cls=DateIso8601Encoder))

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
