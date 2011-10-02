from pyws.errors import AccessDenied

soap_headers_schema = {
    0: 'Headers',
    'username': str,
    'password': str,
}

def authenticate(data):
    if data != {'username': 'user', 'password': 'pass'}:
        raise AccessDenied(data and data.get('username'))
    return data.get('username')
