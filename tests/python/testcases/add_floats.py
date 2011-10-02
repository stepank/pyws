import unittest2 as unittest

from base import BaseTestCaseMixin

class AddFloatsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        self.assertEqual(self.service.add_floats(10.5, 5.3), 15.8)
