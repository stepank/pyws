from suds import null
import unittest2 as unittest

from base import BaseTestCaseMixin

class AddStringDictsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null_args(self):
        res = self.service.add_string_dicts(null(), null())
        self.assertEqual(res.a, None)
        self.assertEqual(res.b, None)

    def test_null(self):
        p = self.factory.create('types:ABStringDict')
        p.a = null()
        p.b = null()
        q = self.factory.create('types:ABStringDict')
        q.a = null()
        q.b = null()
        res = self.service.add_string_dicts(p, q)
        self.assertEqual(res.a, None)
        self.assertEqual(res.b, None)

    def test_empty(self):
        p = self.factory.create('types:ABStringDict')
        p.a = ''
        p.b = ''
        q = self.factory.create('types:ABStringDict')
        q.a = ''
        q.b = ''
        res = self.service.add_string_dicts(p, q)

    def test(self):
        p = self.factory.create('types:ABStringDict')
        p.a = 'hello'
        p.b = 'say'
        q = self.factory.create('types:ABStringDict')
        q.a = ' world'
        q.b = ' hello'
        res = self.service.add_string_dicts(p, q)
        self.assertEqual(res.a, 'hello world')
        self.assertEqual(res.b, 'say hello')
