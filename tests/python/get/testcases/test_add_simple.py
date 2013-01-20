import unittest2 as unittest

from client import make_get_call


class AddSimpleTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(
            make_get_call('add_simple', a='hello', b=' world'), 'hello world')
