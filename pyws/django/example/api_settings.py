from pyws.protocols import RestProtocol, JsonProtocol, SoapProtocol

DEBUG = True

LOCATION = 'http://localhost:8000/api/soap'

PROTOCOLS = {
    'rest': RestProtocol(),
    'json': JsonProtocol(),
    'soap': SoapProtocol('Test', 'http://example.com/'),
}

from pyws.functions.managers import FixedFunctionManager
from pyws.example import simple, simple_integer_adapter, simple_float_adapter,\
    add_integer_adapter, add_float_adapter

FUNCTION_MANAGERS = (
    FixedFunctionManager(
        simple,
        simple_integer_adapter,
        simple_float_adapter,
        add_integer_adapter,
        add_float_adapter
    ),
)