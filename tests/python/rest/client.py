import json

from urllib import urlencode
from urllib2 import urlopen, HTTPError


def encode_arg((name, value)):
    if isinstance(value, (list, tuple)):
        return '&'.join(urlencode({name: element}) for element in value)
    return urlencode({name: value})


def encode_args(args):
    return '&'.join(map(encode_arg, args.iteritems()))


def make_rest_call(func, **args):
    try:
        return json.loads(urlopen(
            'http://127.0.0.1:8000/api/rest/%s?%s' % (func, encode_args(args))
        ).read())['result']
    except HTTPError, e:
        raise Exception(json.loads(e.read())['error']['message'])
