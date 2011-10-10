import unittest2 as unittest

from suds import null

from base import BaseTestCaseMixin

class AddSimpleTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null(self):
        self.assertEqual(
            self.service.add_simple(null(), null()), None)

    def test_empty(self):
        self.assertEqual(
            self.service.add_simple('', ''), None)

    def test(self):
        self.assertEqual(
            self.service.add_simple('hello', ' world'), 'hello world')
