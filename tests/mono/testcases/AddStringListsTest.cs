using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddStringListsTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            string[] r = service.add_string_lists(null, null);
            Assert.AreEqual(0, r.Length);
        }

        [Test()]
        public void test_empty() {
            string[] a1 = {};
            string[] a2 = {};
            string[] r = service.add_string_lists(a1, a2);
            Assert.AreEqual(0, r.Length);
        }

        [Test()]
        public void test_null_value() {
            string[] a1 = {null};
            string[] a2 = {null};
            string[] r = service.add_string_lists(a1, a2);
            // That's weird... The client sends an empty array,
            // hence it receives an empty array as well
            Assert.AreEqual(0, r.Length);
        }

        [Test()]
        public void test_empty_value() {
            string[] a1 = {""};
            string[] a2 = {""};
            string[] r = service.add_string_lists(a1, a2);
            Assert.AreEqual(1, r.Length);
            Assert.AreEqual("", r[0]);
        }

        [Test()]
        public void test_equal_size() {
            string[] a1 = {"a", "b", "c"};
            string[] a2 = {"d", "e", "f"};
            string[] r = service.add_string_lists(a1, a2);
            Assert.AreEqual(r.Length, 3);
            Assert.AreEqual("ad", r[0]);
            Assert.AreEqual("be", r[1]);
            Assert.AreEqual("cf", r[2]);
        }

        [Test()]
        public void test_diff_size() {
            string[] a1 = {"a", "b", "c"};
            string[] a2 = {"d", "e", "f", "g", "h"};
            string[] r = service.add_string_lists(a1, a2);
            Assert.AreEqual(r.Length, 5);
            Assert.AreEqual("ad", r[0]);
            Assert.AreEqual("be", r[1]);
            Assert.AreEqual("cf", r[2]);
            Assert.AreEqual("g", r[3]);
            Assert.AreEqual("h", r[4]);
        }
    }
}
