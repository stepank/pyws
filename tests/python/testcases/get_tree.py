import unittest2 as unittest

from base import BaseTestCaseMixin

class GetTreeTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_none_ret(self):
        self.assertEqual(self.service.get_tree(0), None)

    def test_notset(self):
        res = self.service.get_tree(1)
        self.assertEqual(res.value, 1)
        self.assertFalse(hasattr(res, 'left'))
        self.assertFalse(hasattr(res, 'right'))

    def test_none(self):
        res = self.service.get_tree(2)
        self.assertEqual(res.value, 2)
        self.assertEqual(res.left, None)
        self.assertEqual(res.right, None)

    def test_none(self):
        res = self.service.get_tree(3)
        self.assertEqual(res.value, 3)
        self.assertEqual(res.left.value, 4)
        self.assertEqual(res.left.left, None)
        self.assertEqual(res.left.right, None)
        self.assertEqual(res.right.value, 5)
        self.assertEqual(res.right.left, None)
        self.assertEqual(res.right.right, None)
