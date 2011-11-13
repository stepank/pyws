from wsgiref.simple_server import make_server

import os, sys
dirname = os.path.dirname(__file__)
sys.path += [
    os.path.abspath(os.path.join(dirname, '..')),
    os.path.abspath(os.path.join(dirname, '..', '..', 'src')),
]

from pyws.adapters._wsgi import create_application

from server import server

httpd = make_server('', 8000, create_application(server, 'api/'))
httpd.serve_forever()
