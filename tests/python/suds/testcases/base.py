from factory import build_client


class BaseTestCaseMixin(object):

    def setUp(self):
        client = build_client()
        self.client = client
        self.service = client.service
        self.factory = client.factory
