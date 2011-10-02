import unittest2 as unittest

from base import BaseTestCaseMixin

class AddIntegerDictsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        q = self.factory.create('types:ABIntegerDict')
        q.a = 100
        q.b = 50
        p = self.factory.create('types:ABIntegerDict')
        p.a = 50
        p.b = 25
        res = self.service.add_integer_dicts(q, p)
        self.assertEqual(res.a, 150)
        self.assertEqual(res.b, 75)
