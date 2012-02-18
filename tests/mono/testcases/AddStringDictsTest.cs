using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddStringDictsTest : TestServiceTest {

        [Test()]
        public void test_null_args() {
            ABStringDict r = service.add_string_dicts(null, null);
            Assert.AreEqual("", r.a);
            Assert.AreEqual("", r.b);
        }

        [Test()]
        public void test_notset() {
            ABStringDict r = service.add_string_dicts(
                new ABStringDict(), new ABStringDict());
            Assert.AreEqual("", r.a);
            Assert.AreEqual("", r.b);
        }

        [Test()]
        public void test_null() {
            ABStringDict p = new ABStringDict();
            p.a = null;
            p.b = null;
            ABStringDict q = new ABStringDict();
            q.a = null;
            q.b = null;
            ABStringDict r = service.add_string_dicts(p, q);
            Assert.AreEqual("", r.a);
            Assert.AreEqual("", r.b);
        }

        [Test()]
        public void test_empty() {
            ABStringDict p = new ABStringDict();
            p.a = "";
            p.b = "";
            ABStringDict q = new ABStringDict();
            q.a = "";
            q.b = "";
            ABStringDict r = service.add_string_dicts(p, q);
            Assert.AreEqual("", r.a);
            Assert.AreEqual("", r.b);
        }

        [Test()]
        public void test() {
            ABStringDict p = new ABStringDict();
            p.a = "hello ";
            p.b = "say ";
            ABStringDict q = new ABStringDict();
            q.a = "world";
            q.b = "hello";
            ABStringDict r = service.add_string_dicts(p, q);
            Assert.AreEqual("hello world", r.a);
            Assert.AreEqual("say hello", r.b);
        }
    }
}
