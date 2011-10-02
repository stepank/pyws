import suds
import unittest2 as unittest

from base import BaseTestCaseMixin

class RaisesExceptionTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        try:
            self.service.raises_exception()
        except suds.WebFault, e:
            self.assertEqual(e.fault.faultstring, 'hello error')
            return
        self.assertTrue(False, 'Exception hasn\'t been thrown')
