import json
import requests


class RestClient(object):

    def __getattr__(self, name):
        def func(route, *args, **kwargs):
            response = getattr(requests, name)(
                'http://localhost:8000/api/rest/%s' % route, *args, **kwargs)
            return json.loads(response.text)['result']
        return func
