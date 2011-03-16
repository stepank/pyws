from django.http import HttpResponse

from pyws.request import Request

def serve(request, tail, server):

    request = Request(tail,
        request.raw_post_data, request.GET, request.POST, request.COOKIES)

    response = server.process_request(request)

    return HttpResponse(response.text)