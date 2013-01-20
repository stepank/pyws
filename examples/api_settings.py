from pyws.protocols import GetProtocol, JsonProtocol

from authenticate import authenticate, soap_headers_schema

DEBUG = True

PROTOCOLS = (
    GetProtocol(),
    JsonProtocol(),
)

SOAP_PROTOCOL_PARAMS = (
    'Test',
    'http://example.com/',
    'http://localhost:8000/api/soap',
    soap_headers_schema
)

CREATE_CONTEXT = authenticate
