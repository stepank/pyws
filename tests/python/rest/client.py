from pyws.utils import json

from urllib import urlencode
from urllib2 import urlopen, HTTPError, Request


def encode_arg((name, value)):
    if isinstance(value, (list, tuple)):
        return '&'.join(urlencode({name: element}) for element in value)
    return urlencode({name: value})


def encode_args(args):
    return '&'.join(map(encode_arg, args.iteritems()))


def make_rest_call(func, headers=None, **args):
    request = Request(
        'http://127.0.0.1:8000/api/rest/%s?%s' % (func, encode_args(args)),
        headers=headers or {},
    )
    try:
        return json.loads(urlopen(request).read())['result']
    except HTTPError, e:
        raise Exception(json.loads(e.read())['error']['message'])
