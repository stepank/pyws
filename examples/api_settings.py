from pyws.protocols import GetProtocol, JsonProtocol, RestProtocol

from authenticate import authenticate, soap_headers_schema

DEBUG = True

PROTOCOLS = (
    GetProtocol(),
    JsonProtocol(),
    RestProtocol(),
)

SOAP_PROTOCOL_PARAMS = (
    'Test',
    'http://example.com/',
    'http://localhost:8000/api/soap',
    soap_headers_schema
)

CREATE_CONTEXT = authenticate
