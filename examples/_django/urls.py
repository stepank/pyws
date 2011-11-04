from django.conf.urls.defaults import patterns, url

from pyws.adapters._django import serve

from server import server
from _django.test_form import test_form

urlpatterns = patterns('',
    url('^$', test_form),
    url('^api/(.*)', serve, {'server': server})
)
