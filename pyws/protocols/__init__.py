from pyws.response import Response


class Protocol(object):

    def __init__(self, *args, **kwargs):
        pass

    def get_function(self, request):
        raise NotImplemented('Protocol.get_function')


class SoapProtocol(Protocol):

    def get_function(self, request):

        if request.tail == 'wsdl':
            return self.get_wsdl

        return 'simple', {'s': 'hello'}

    def get_wsdl(self, request):
        return Response('wsdl')


class RestProtocol(Protocol):

    def get_function(self, request):
        return request.tail, request.GET

    def get_response(self, result):
        return Response(result)
