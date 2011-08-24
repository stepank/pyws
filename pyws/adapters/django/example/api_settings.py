from pyws.protocols import RestProtocol, JsonProtocol, \
    HeadersAuthDataGetter

from authenticate import authenticate, soap_headers_schema

DEBUG = True

PROTOCOLS = (
    RestProtocol(),
    JsonProtocol(),
)

SOAP_PROTOCOL_PARAMS = (
    'Test', 'http://example.com/', 'http://localhost:8000/api/soap',
    HeadersAuthDataGetter(soap_headers_schema))

AUTHENTICATOR = authenticate
