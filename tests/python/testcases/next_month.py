import unittest2 as unittest

from datetime import date, datetime

from base import BaseTestCaseMixin

class NextMonthTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test(self):
        self.assertEqual(
            self.service.next_month(date(2011, 8, 20)), date(2011, 9, 20))

    def test_dt(self):
        self.assertEqual(
            self.service.next_month_dt(datetime(2011, 8, 20, 0, 4, 59)),
            datetime(2011, 9, 20, 0, 4, 59))
