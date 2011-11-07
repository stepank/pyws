from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pyws.request import Request

@csrf_exempt
def serve(request, tail, server):

    request = Request(tail,
        request.raw_post_data if not request.GET else '',
        request.GET, request.POST, request.COOKIES)

    response = server.process_request(request)

    return HttpResponse(response.text, content_type=response.content_type)
