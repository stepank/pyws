from pyws.protocols import RestProtocol, JsonProtocol, \
    HeadersAuthDataGetter

from authenticate import authenticate, soap_headers_schema

DEBUG = True

LOCATION = 'http://localhost:8000/api/'

PROTOCOLS = (
    RestProtocol(),
    JsonProtocol(),
)

SOAP_PROTOCOL_PARAMS = (
    'Test', 'http://example.com/', HeadersAuthDataGetter(soap_headers_schema))

AUTHENTICATOR = authenticate

from pyws.functions.managers import FixedFunctionManager
from pyws.example import *

FUNCTION_MANAGERS = (
    FixedFunctionManager(
        add_simple,
        add_integers_adapter,
        add_floats_adapter,
        next_month_adapter,
        next_month_dt_adapter,
        add_string_dicts_adapter,
        add_integer_dicts_adapter,
        add_string_lists_adapter,
        add_integer_lists_adapter,
        sum_tree_adapter,
        get_tree_adapter,
        needs_auth_adapter,
        raises_exception,
    ),
)
