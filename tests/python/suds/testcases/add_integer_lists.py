import unittest2 as unittest

from base import BaseTestCaseMixin

class AddIntegerListsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_empty(self):
        p = self.factory.create('types:IntegerList')
        p.item = []
        q = self.factory.create('types:IntegerList')
        q.item = []
        res = self.service.add_integer_lists(p, q)

    def test(self):
        p = self.factory.create('types:IntegerList')
        p.item = [1, 2, 3]
        q = self.factory.create('types:IntegerList')
        q.item = [3, -5, 0]
        res = self.service.add_integer_lists(p, q)
        self.assertEqual(res.item, [4, -3, 3])

    def test_diff_size(self):
        p = self.factory.create('types:IntegerList')
        p.item = [1, 2, 3]
        q = self.factory.create('types:IntegerList')
        q.item = [3, -5, 0, 11, -5]
        res = self.service.add_integer_lists(p, q)
        self.assertEqual(res.item, [4, -3, 3, 11, -5])
