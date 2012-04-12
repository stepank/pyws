import unittest2 as unittest

from client import make_rest_call


class AddIntegersTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(make_rest_call('add_integers', a=100, b=50), 150)
