from pyws.protocols import RestProtocol, SoapProtocol

PROTOCOLS = {
    'rest': RestProtocol,
    'soap': SoapProtocol,
}

from pyws.functions.managers import FixedFunctionManager
from pyws.example import simple, simple_integer_adapter, simple_float_adapter

FUNCTION_MANAGERS = (
    FixedFunctionManager(
        simple, simple_integer_adapter, simple_float_adapter),
)