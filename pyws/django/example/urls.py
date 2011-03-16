from django.conf.urls.defaults import *

from pyws.server import Server

import api_settings

urlpatterns = patterns('',
    url('^api/(.*)', 'pyws.django.serve', {'server': Server(api_settings)})
)
