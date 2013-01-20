import re

from datetime import date, datetime
from functools import partial

from pyws.errors import BadRequest
from pyws.functions.args.types.complex import List
from pyws.response import Response
from pyws.utils import json, cached_property
from pyws.protocols.base import Protocol, Route, NameRoute

__all__ = ('GetProtocol', 'JsonProtocol', 'RestProtocol', 'UrlRoute', 'url')


class DateIso8601Encoder(json.JSONEncoder):
    # JSON Serializer with datetime support
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


create_response = partial(Response, content_type='application/json')
create_error_response = partial(create_response, status=Response.STATUS_ERROR)


class GetProtocol(Protocol):

    name = 'get'

    def get_function(self, request):
        return NameRoute(request.tail)

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


class JsonProtocol(GetProtocol):

    name = 'json'

    def get_arguments(self, request, arguments):
        if not request.text:
            return {}
        try:
            return json.loads(request.text)
        except ValueError:
            raise BadRequest()


NON_LETTERS_RE = re.compile('\W')


class RestProtocol(JsonProtocol):

    name = 'rest'

    def get_function(self, request):
        return url(request.method, request.tail)

    def get_arguments(self, request, arguments):
        args = GetProtocol.get_arguments(self, request, arguments)
        args.update(JsonProtocol.get_arguments(self, request, arguments))
        return args


class UrlRoute(Route):

    protocols = [RestProtocol]

    def __init__(self, method, route):
        self.method = method
        self.route = route

    def __str__(self):
        return '<UrlRoute(%s, %s)>' % (self.method, self.route)

    @property
    def name(self):
        return self.method + '_' + NON_LETTERS_RE.sub('_', self.route)

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.method == other.method and self.route == other.route

    @cached_property
    def re(self):
        return re.compile(self.route)

    def match(self, other):
        if self.method == other.method:
            match = self.re.match(other.route)
            if match:
                return True, match.groupdict()
        return False, {}


def url(*args, **kwargs):
    return UrlRoute(*args, **kwargs)
