using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class GetTreeTest : TestServiceTest {

        [Test()]
        public void test_null_ret() {
            Assert.AreEqual(null, service.get_tree(0));
        }

        [Test()]
        public void test_notset() {
            Tree r = service.get_tree(1);
            Assert.AreEqual(1, r.value);
            Assert.AreEqual(null, r.left);
            Assert.AreEqual(null, r.right);
        }

        [Test()]
        public void test_null() {
            Tree r = service.get_tree(2);
            Assert.AreEqual(2, r.value);
            Assert.AreEqual(null, r.left);
            Assert.AreEqual(null, r.right);
        }

        [Test()]
        public void test() {
            Tree r = service.get_tree(3);
            Assert.AreEqual(3, r.value);
            Assert.AreEqual(4, r.left.value);
            Assert.AreEqual(null, r.left.left);
            Assert.AreEqual(null, r.left.right);
            Assert.AreEqual(5, r.right.value);
            Assert.AreEqual(null, r.right.left);
            Assert.AreEqual(null, r.right.right);
        }
    }
}
