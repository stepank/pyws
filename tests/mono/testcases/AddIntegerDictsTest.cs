using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddIntegerDictsTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            ABIntegerDict r = service.add_integer_dicts(null, null);
            Assert.AreEqual(0, r.a);
            Assert.AreEqual(0, r.b);
        }

        [Test()]
        public void test_notset() {
            ABIntegerDict r = service.add_integer_dicts(
                new ABIntegerDict(), new ABIntegerDict());
            Assert.AreEqual(0, r.a);
            Assert.AreEqual(0, r.b);
        }

        [Test()]
        public void test_null() {
            ABIntegerDict p = new ABIntegerDict();
            p.a = null;
            p.b = null;
            ABIntegerDict q = new ABIntegerDict();
            q.a = null;
            q.b = null;
            ABIntegerDict r = service.add_integer_dicts(p, q);
            Assert.AreEqual(0, r.a);
            Assert.AreEqual(0, r.b);
        }

        [Test()]
        public void test_empty() {
            ABIntegerDict p = new ABIntegerDict();
            p.a = 0;
            p.b = 0;
            ABIntegerDict q = new ABIntegerDict();
            q.a = 0;
            q.b = 0;
            ABIntegerDict r = service.add_integer_dicts(p, q);
            Assert.AreEqual(0, r.a);
            Assert.AreEqual(0, r.b);
        }

        [Test()]
        public void test() {
            ABIntegerDict p = new ABIntegerDict();
            p.a = 100;
            p.b = 50;
            ABIntegerDict q = new ABIntegerDict();
            q.a = 50;
            q.b = 25;
            ABIntegerDict r = service.add_integer_dicts(p, q);
            Assert.AreEqual(150, r.a);
            Assert.AreEqual(75, r.b);
        }
    }
}
