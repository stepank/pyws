using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddIntegerListsTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            int[] r = service.add_integer_lists(null, null);
            Assert.AreEqual(r.Length, 0);
        }

        [Test()]
        public void test_empty() {
            int[] a1 = {};
            int[] a2 = {};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(r.Length, 0);
        }

        [Test()]
        public void test_empty_value() {
            int[] a1 = {0};
            int[] a2 = {0};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(r.Length, 1);
            Assert.AreEqual(r[0], 0);
        }

        [Test()]
        public void test_equal_size() {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(r.Length, 3);
            Assert.AreEqual(r[0], 4);
            Assert.AreEqual(r[1], -3);
            Assert.AreEqual(r[2], 3);
        }

        [Test()]
        public void test_diff_size() {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0, 11, -5};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(r.Length, 5);
            Assert.AreEqual(r[0], 4);
            Assert.AreEqual(r[1], -3);
            Assert.AreEqual(r[2], 3);
            Assert.AreEqual(r[3], 11);
            Assert.AreEqual(r[4], -5);
        }
    }
}
