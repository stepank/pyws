import unittest2 as unittest

from base import BaseTestCaseMixin

class AddSimpleTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        self.assertEqual(
            self.service.add_simple('hello', ' world'), 'hello world')
