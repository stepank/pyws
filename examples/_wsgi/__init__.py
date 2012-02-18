#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG)

from wsgiref.simple_server import make_server

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyws.adapters._wsgi import create_application

from server import server

httpd = make_server('', 8000, create_application(server, 'api/'))
httpd.serve_forever()
