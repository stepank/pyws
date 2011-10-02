import unittest2 as unittest

from base import BaseTestCaseMixin

class AddStringListsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        q = self.factory.create('types:StringList')
        q.item = ['a', 'b', 'c']
        p = self.factory.create('types:StringList')
        p.item = ['d', 'e', 'f']
        res = self.service.add_string_lists(q, p)
        self.assertEqual(res.item, ['ad', 'be', 'cf'])

    def test_diff_size(self):
        q = self.factory.create('types:StringList')
        q.item = ['a', 'b', 'c']
        p = self.factory.create('types:StringList')
        p.item = ['d', 'e', 'f', 'g', 'h']
        res = self.service.add_string_lists(q, p)
        self.assertEqual(res.item, ['ad', 'be', 'cf', 'g', 'h'])
