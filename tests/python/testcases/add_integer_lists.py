import unittest2 as unittest

from base import BaseTestCaseMixin

class AddIntegerListsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        q = self.factory.create('types:IntegerList')
        q.item = [1, 2, 3]
        p = self.factory.create('types:IntegerList')
        p.item = [3, -5, 0]
        res = self.service.add_integer_lists(q, p)
        self.assertEqual(res.item, [4, -3, 3])

    def test_diff_size(self):
        q = self.factory.create('types:IntegerList')
        q.item = [1, 2, 3]
        p = self.factory.create('types:IntegerList')
        p.item = [3, -5, 0, 11, -5]
        res = self.service.add_integer_lists(q, p)
        self.assertEqual(res.item, [4, -3, 3, 11, -5])
