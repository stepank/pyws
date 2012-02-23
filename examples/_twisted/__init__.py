#!/usr/bin/env python

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
