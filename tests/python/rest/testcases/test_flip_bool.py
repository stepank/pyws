import unittest2 as unittest

from client import make_rest_call


class FlipBoolTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(make_rest_call('flip_boolean', b=False), True)
        self.assertEquals(make_rest_call('flip_boolean', b=True), False)
