using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddIntegerListsTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            int[] r = service.add_integer_lists(null, null);
            Assert.AreEqual(0, r.Length);
        }

        [Test()]
        public void test_empty() {
            int[] a1 = {};
            int[] a2 = {};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(0, r.Length);
        }

        [Test()]
        public void test_empty_value() {
            int[] a1 = {0};
            int[] a2 = {0};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(1, r.Length);
            Assert.AreEqual(0, r[0]);
        }

        [Test()]
        public void test_equal_size() {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(r.Length, 3);
            Assert.AreEqual(4, r[0]);
            Assert.AreEqual(-3, r[1]);
            Assert.AreEqual(3, r[2]);
        }

        [Test()]
        public void test_diff_size() {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0, 11, -5};
            int[] r = service.add_integer_lists(a1, a2);
            Assert.AreEqual(5, r.Length);
            Assert.AreEqual(4, r[0]);
            Assert.AreEqual(-3, r[1]);
            Assert.AreEqual(3, r[2]);
            Assert.AreEqual(11, r[3]);
            Assert.AreEqual(-5, r[4]);
        }
    }
}
