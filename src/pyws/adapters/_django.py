from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pyws.adapters import get_http_response_code_num
from pyws.request import Request

@csrf_exempt
def serve(request, tail, server):
    """
    Django adapter. It has three arguments:

    #. ``request`` is a Django request object,
    #. ``tail`` is everything that's left from an URL, which adapter is
       attached to,
    #. ``server`` is a pyws server object.

    First two are the context of an application, function ``serve`` transforms
    them into a pyws request object. Then it feeds the request to the server,
    gets the response and transforms it into a Django response object.
    """

    request = Request(tail,
        request.raw_post_data if not request.GET else '',
        request.GET, request.POST, request.COOKIES)

    response = server.process_request(request)

    return HttpResponse(
        response.text, content_type=response.content_type,
        status=get_http_response_code_num(response))
