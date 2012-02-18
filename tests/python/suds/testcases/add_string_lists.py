import unittest2 as unittest

from base import BaseTestCaseMixin

class AddStringListsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_empty(self):
        p = self.factory.create('types:StringList')
        p.item = []
        q = self.factory.create('types:StringList')
        q.item = []
        res = self.service.add_string_lists(p, q)

    def test(self):
        p = self.factory.create('types:StringList')
        p.item = ['a', 'b', 'c']
        q = self.factory.create('types:StringList')
        q.item = ['d', 'e', 'f']
        res = self.service.add_string_lists(p, q)
        self.assertEqual(res.item, ['ad', 'be', 'cf'])

    def test_diff_size(self):
        p = self.factory.create('types:StringList')
        p.item = ['a', 'b', 'c']
        q = self.factory.create('types:StringList')
        q.item = ['d', 'e', 'f', 'g', 'h']
        res = self.service.add_string_lists(p, q)
        self.assertEqual(res.item, ['ad', 'be', 'cf', 'g', 'h'])
