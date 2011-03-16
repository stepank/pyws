from pyws.protocols import RestProtocol, SoapProtocol

PROTOCOLS = {
    'rest': RestProtocol,
    'soap': SoapProtocol,
}

from pyws.functions.managers import FixedFunctionManager
from pyws.example import simple

FUNCTION_MANAGERS = (
    FixedFunctionManager(simple),
)