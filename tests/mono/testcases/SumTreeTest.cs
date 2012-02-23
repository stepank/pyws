using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class SumTreeTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            Assert.AreEqual(0, service.sum_tree(null));
        }

        [Test()]
        public void test_notset() {
            Assert.AreEqual(0, service.sum_tree(new Tree()));
        }

        [Test()]
        public void test_null() {
            Tree p = new Tree();
            p.value = null;
            p.left = null;
            p.right = null;
            Assert.AreEqual(0, service.sum_tree(p));
        }

        [Test()]
        public void test_value() {
            Tree p = new Tree();
            p.value = 10;
            p.left = null;
            p.right = null;
            Assert.AreEqual(10, service.sum_tree(p));
        }

        [Test()]
        public void test() {
            Tree l = new Tree();
            l.value = 20;
            Tree r = new Tree();
            r.value = 30;
            Tree p = new Tree();
            p.value = 10;
            p.left = l;
            p.right = r;
            Assert.AreEqual(60, service.sum_tree(p));
        }
    }
}
