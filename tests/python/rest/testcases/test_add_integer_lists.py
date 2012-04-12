import unittest2 as unittest

from client import make_rest_call


class AddIntegerListsTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEquals(
            make_rest_call('add_integer_lists', p=[], q=[]), [])

    def test_one(self):
        self.assertEquals(
            make_rest_call('add_integer_lists', p=[1], q=[2]), [3])

    def test_simple(self):
        self.assertEquals(
            make_rest_call('add_integer_lists', p=[1, 2, 3], q=[3, -5, 0]),
            [4, -3, 3])

    def test_diff_size(self):
        self.assertEquals(
            make_rest_call(
                'add_integer_lists', p=[1, 2, 3], q=[3, -5, 0, 11, -5]),
            [4, -3, 3, 11, -5])
