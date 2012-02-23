import os
import suds

wsdl_path = os.path.abspath(os.path.dirname(__file__)) + '/test.wsdl'

def build_client():
    return suds.client.Client('file://%s' % wsdl_path, cache=None)
