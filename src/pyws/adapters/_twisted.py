from pyws.request import Request

def serve(request, server):
    """
    Twisted Web adapter. It has two arguments:

    #. a Twisted Web request object,
    #. a pyws server object.

    First one is the context of an application, function ``serve`` transforms
    it into a pyws request object. Then it feeds the request to the server,
    gets a response, sets header ``Content-Type`` and returns response text.
    """

    request_ = Request('/'.join(request.postpath),
        request.content.read() if not request.method == 'GET' else '',
        request.args, request.args, {})

    response = server.process_request(request_)

    request.setHeader('Content-Type', response.content_type)

    return response.text
