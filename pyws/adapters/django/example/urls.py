import urlparse

from django.conf.urls.defaults import * #@UnusedWildImport
from django.http import HttpRequest
from django.shortcuts import render_to_response

from pyws.adapters.django import serve
from pyws.server import SoapServer

import api_settings

server = SoapServer(api_settings, *api_settings.SOAP_PROTOCOL_PARAMS)

# Just import the example module to register all its functions
#noinspection PyUnresolvedReferences
import pyws.example

PROTOCOLS = (
  ('rest', 'REST'),
  ('json', 'JSON'),
  ('soap', 'SOAP'),
)


def test_form(request):

    data = {
        'protocols': PROTOCOLS,
    }

    if request.method == 'POST':

        tail = request.POST['tail']
        protocol = request.POST['protocol']
        query_string = request.POST['query_string']
        request_text = request.POST['request']

        fake_request = HttpRequest()
        fake_request.GET = urlparse.parse_qs(query_string)
        if not query_string:
            fake_request._raw_post_data = request_text

        response = serve(fake_request, protocol + '/' + tail, server)

        data.update({
            'tail': tail,
            'protocol': protocol,
            'query_string': query_string,
            'request': request_text,
            'response': response,
        })

    return render_to_response('test_form.html', data)

urlpatterns = patterns('',
    url('^$', test_form),
    url('^api/(.*)', serve, {'server': server})
)
