from factory import build_client
from rest_client import RestClient


class BaseTestCaseMixin(object):

    def setUp(self):
        client = build_client()
        self.client = client
        self.service = client.service
        self.factory = client.factory
        self.rest_client = RestClient()
