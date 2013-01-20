import os

import suds

from rest_client import RestClient

wsdl_path = os.path.realpath(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '..', 'test.wsdl'))


class BaseTestCaseMixin(object):

    def setUp(self):
        self.client = suds.client.Client('file://%s' % wsdl_path, cache=None)
        self.service = self.client.service
        self.factory = self.client.factory
        self.rest_client = RestClient()
