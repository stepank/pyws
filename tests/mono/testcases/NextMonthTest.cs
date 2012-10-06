using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class NextMonthTest : TestServiceTest {

        DateTime origin = new DateTime(1970, 1, 1, 0, 0, 0, 0);

        public DateTime from_timestamp(long timestamp) {
            return origin.AddSeconds(timestamp);
        }

        public long to_timestamp(DateTime date) {
            return (long)((date - origin).TotalSeconds);
        }

        [Test()]
        public void test_null() {
            Assert.AreEqual(null, service.next_month(null));
        }

        [Test()]
        public void test() {
            // The client sends datetime instead of just date.
            // There are two problems with such a behaviour:
            // 1. Need to parse datetime instaed of date, not a problem
            //    actually.
            // 2. It sends datetime in UTC timezone and it results in a shifted
            //    date value. And this is the problem.
        }

        [Test()]
        public void test_dt_null() {
            Assert.AreEqual(null, service.next_month_dt(null));
        }

        [Test()]
        public void test_dt() {
            Assert.AreEqual(
                new DateTime(2011, 9, 20, 7, 41, 25),
                service.next_month_dt(
                    new DateTime(2011, 8, 20, 7, 41, 25)).Value);
        }
    }
}
