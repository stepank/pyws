# coding=utf-8

import unittest2 as unittest

from suds import null

from testcases.base import BaseTestCaseMixin


class AddSimpleTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_null(self):
        self.assertEqual(
            self.service.add_simple(null(), null()), None)

    def test_empty(self):
        self.assertEqual(
            self.service.add_simple('', ''), None)

    def test_simple(self):
        self.assertEqual(
            self.service.add_simple('hello', ' world'), 'hello world')

    def test_unicode(self):
        self.assertEqual(
            self.service.add_simple('hello', u' лопата'), u'hello лопата')
