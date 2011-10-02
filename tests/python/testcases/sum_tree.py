import unittest2 as unittest

from base import BaseTestCaseMixin

class SumTreeTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_value(self):
        p = self.factory.create('types:Tree')
        p.value = 10
        p.left = None
        p.right = None
        self.assertEqual(self.service.sum_tree(p), 10)

    def test(self):
        p = self.factory.create('types:Tree')
        p.value = 10
        p.left = self.factory.create('types:Tree')
        p.left.value = 20
        p.left.left = None
        p.left.right = None
        p.right = self.factory.create('types:Tree')
        p.right.value = 30
        p.right.left = None
        p.right.right = None
        self.assertEqual(self.service.sum_tree(p), 60)
