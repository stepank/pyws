import os
import suds

class BaseTestCaseMixin(object):

    def setUp(self):
        url = os.path.abspath(os.path.dirname(__file__) + '/..') + '/test.wsdl'
        self.client = suds.client.Client('file://%s' % url, cache=None)
        self.service = self.client.service
        self.factory = self.client.factory
