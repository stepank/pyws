from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import os, sys
dirname = os.path.dirname(__file__)
sys.path += [
    os.path.abspath(os.path.join(dirname, '..')),
    os.path.abspath(os.path.join(dirname, '..', '..', 'src')),
]

from pyws.adapters._twisted import serve

from server import server


class Simple(Resource):

    isLeaf = True

    def render(self, request):
        request.postpath = request.postpath[1:]
        return serve(request, server)


#noinspection PyUnresolvedReferences
reactor.listenTCP(8000, Site(Simple()))
#noinspection PyUnresolvedReferences
reactor.run()
