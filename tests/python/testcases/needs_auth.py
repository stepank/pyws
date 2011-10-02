import suds
import unittest2 as unittest

from base import BaseTestCaseMixin

class RaisesExceptionTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        headers = self.factory.create('types:Headers')
        headers.username = 'user'
        headers.password = 'pass'
        self.client.set_options(soapheaders=headers)
        self.assertEqual(self.service.say_hello(), 'hello user')

    def _test_exception(self, message):
        try:
            self.service.say_hello()
        except suds.WebFault, e:
            self.assertEqual(e.fault.faultstring, message)
            return
        self.assertTrue(False, 'Exception hasn\'t been thrown')

    def test_none_exception(self):
        self._test_exception('Access denied')

    def test_exception(self):
        headers = self.factory.create('types:Headers')
        headers.username = 'fake'
        headers.password = 'pass'
        self.client.set_options(soapheaders=headers)
        self._test_exception('Access denied for user fake')
