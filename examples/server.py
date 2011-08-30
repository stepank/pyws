from pyws.server import SoapServer

import api_settings

server = SoapServer(api_settings, *api_settings.SOAP_PROTOCOL_PARAMS)

# Just import the example module to register all its functions
#noinspection PyUnresolvedReferences
import functions
