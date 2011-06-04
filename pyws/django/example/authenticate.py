from pyws.errors import AccessDenied
from pyws.functions.args import DictOf, String

soap_headers_schema = DictOf('HeadersDict',
    ('username', String),
    ('password', String),
)

def authenticate(data):
    if not data.get('username') == 'user' or \
            not data.get('password') == 'pass':
        raise AccessDenied(data.get('username'))
