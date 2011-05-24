from pyws.protocols import RestProtocol, JsonProtocol, SoapProtocol

DEBUG = True

LOCATION = 'http://localhost:8000/api/soap'

PROTOCOLS = {
    'rest': RestProtocol(),
    'json': JsonProtocol(),
    'soap': SoapProtocol('Test', 'http://example.com/'),
}

from pyws.functions.managers import FixedFunctionManager
from pyws.example import * #@UnusedWildImport

FUNCTION_MANAGERS = (
    FixedFunctionManager(
        add_simple,
        add_integers_adapter,
        add_floats_adapter,
        add_string_dicts_adapter,
        add_integer_dicts_adapter,
        add_string_lists_adapter,
        add_integer_lists_adapter,
        sum_tree_adapter,
        get_tree_adapter,
    ),
)