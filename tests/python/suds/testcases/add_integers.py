import unittest2 as unittest

from suds import null

from base import BaseTestCaseMixin

class AddIntegersTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null(self):
        self.assertEqual(
            self.service.add_integers(null(), null()), 0)

    def test_empty(self):
        self.assertEqual(
            self.service.add_integers(0, 0), 0)

    def test(self):
        self.assertEqual(self.service.add_integers(100, 50), 150)
