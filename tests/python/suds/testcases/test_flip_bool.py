from suds import null
import unittest2 as unittest

from testcases.base import BaseTestCaseMixin


class FlipBoolTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null(self):
        self.assertEqual(self.service.flip_boolean(null()), True)

    def test_numeric(self):
        self.assertEqual(self.service.flip_boolean(0), True)

    def test_simple(self):
        self.assertEqual(self.service.flip_boolean(True), False)
        self.assertEqual(self.service.flip_boolean(False), True)
