from pyws.errors import AccessDenied, BadAuthData
from pyws.functions.args import DictOf, String
from pyws.protocols.soap import SoapProtocol, xml2obj

soap_headers_schema = DictOf('HeadersDict',
    ('username', String),
    ('password', String),
)

def soap_auth_data_getter(request):

    env = request.parsed_data.xml. \
        xpath('/se:Envelope', namespaces=SoapProtocol.namespaces)[0]

    header = env.xpath('./se:Header', namespaces=SoapProtocol.namespaces)
    if len(header) != 1:
        raise BadAuthData()
    header = header[0]

    return xml2obj(header, soap_headers_schema)

def authenticate(data):
    print data
    if not data.get('username') == 'user' or \
            not data.get('password') == 'pass':
        raise AccessDenied(data.get('username'))
