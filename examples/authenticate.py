from pyws.errors import AccessDenied

soap_headers_schema = {
    0: 'Headers',
    'username': str,
    'password': str,
}

def authenticate(data):
    if not data.get('username') == 'user' or \
            not data.get('password') == 'pass':
        raise AccessDenied(data.get('username'))
