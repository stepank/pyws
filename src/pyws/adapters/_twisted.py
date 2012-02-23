from pyws.adapters import get_http_response_code_num
from pyws.request import Request

def serve(request, server):
    """
    Twisted Web adapter. It has two arguments:

    #. ``request`` is a Twisted Web request object,
    #. ``server`` is a pyws server object.

    First one is the context of an application, function ``serve`` transforms
    it into a pyws request object. Then it feeds the request to the server,
    gets the response, sets header ``Content-Type`` and returns response text.
    """

    request_ = Request('/'.join(request.postpath),
        request.content.read() if not request.method == 'GET' else '',
        request.args, request.args, {})

    response = server.process_request(request_)

    request.setHeader('Content-Type', response.content_type)
    request.setResponseCode(get_http_response_code_num(response))

    return response.text
