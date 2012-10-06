import unittest2 as unittest

from client import make_rest_call


class NextMonthTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            make_rest_call('next_month', d='2011-08-20'), '2011-09-20')

    def test_dt(self):
        self.assertEqual(
            make_rest_call('next_month_dt', d='2011-08-20T00:04:59'),
            '2011-09-20T00:04:59+00:00')
