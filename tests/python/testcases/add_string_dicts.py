import unittest2 as unittest

from base import BaseTestCaseMixin

class AddStringDictsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        q = self.factory.create('types:ABStringDict')
        q.a = 'hello'
        q.b = 'say'
        p = self.factory.create('types:ABStringDict')
        p.a = ' world'
        p.b = ' hello'
        res = self.service.add_string_dicts(q, p)
        self.assertEqual(res.a, 'hello world')
        self.assertEqual(res.b, 'say hello')
