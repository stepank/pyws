from suds import null
import unittest2 as unittest

from base import BaseTestCaseMixin

class AddFloatsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null(self):
        self.assertEqual(
            self.service.add_floats(null(), null()), 0)

    def test_empty(self):
        self.assertEqual(
            self.service.add_floats(0, 0), 0)

    def test(self):
        self.assertEqual(self.service.add_floats(10.5, 5.3), 15.8)
