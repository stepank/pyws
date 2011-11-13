from urlparse import parse_qs

from wsgiref import util

from pyws.request import Request

def create_application(server, root_url):
    """
    WSGI adapter. It creates a simple WSGI application, that can be used with
    any WSGI server. The arguments are:

    #. ``server`` is a pyws server object,
    #. ``root_url`` is an URL to which the server will be bound.

    An application created by the function transforms WSGI environment into a
    pyws request object. Then it feeds the request to the server, gets the
    response, sets header ``Content-Type`` and returns response text.
    """

    def serve(environ, start_response):

        root = root_url.lstrip('/')

        tail, get = (util.request_uri(environ).split('?') + [''])[:2]
        tail = tail[len(util.application_uri(environ)):]

        result = []

        content_type = 'text/plain'
        if tail.startswith(root):

            tail = tail[len(root):]

            get = parse_qs(get)
            method = environ['REQUEST_METHOD']

            text, post = '', {}
            if method == 'POST':
                text = environ['wsgi.input'].\
                    read(int(environ.get('CONTENT_LENGTH', 0)))
                post = parse_qs(text)

            response = server.process_request(
                Request(tail, text, get, post, {}))

            content_type = response.content_type
            result.append(response.text)

        status = '200 OK'
        headers = [('Content-type', content_type)]
        start_response(status, headers)

        return result

    return serve
