import unittest2 as unittest

from base import BaseTestCaseMixin

class AddIntegersTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        self.assertEqual(self.service.add_integers(100, 50), 150)
