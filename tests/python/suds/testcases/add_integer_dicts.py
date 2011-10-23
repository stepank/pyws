from suds import null
import unittest2 as unittest

from base import BaseTestCaseMixin

class AddIntegerDictsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null_args(self):
        res = self.service.add_integer_dicts(null(), null())
        self.assertEqual(res.a, 0)
        self.assertEqual(res.b, 0)

    def test_null(self):
        p = self.factory.create('types:ABIntegerDict')
        p.a = null()
        p.b = null()
        q = self.factory.create('types:ABIntegerDict')
        q.a = null()
        q.b = null()
        res = self.service.add_integer_dicts(p, q)
        self.assertEqual(res.a, 0)
        self.assertEqual(res.b, 0)

    def test_empty(self):
        p = self.factory.create('types:ABIntegerDict')
        p.a = 0
        p.b = 0
        q = self.factory.create('types:ABIntegerDict')
        q.a = 0
        q.b = 0
        res = self.service.add_integer_dicts(p, q)
        self.assertEqual(res.a, 0)
        self.assertEqual(res.b, 0)

    def test(self):
        p = self.factory.create('types:ABIntegerDict')
        p.a = 100
        p.b = 50
        q = self.factory.create('types:ABIntegerDict')
        q.a = 50
        q.b = 25
        res = self.service.add_integer_dicts(p, q)
        self.assertEqual(res.a, 150)
        self.assertEqual(res.b, 75)
