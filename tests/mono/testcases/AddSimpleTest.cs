using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddSimpleTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual("", service.add_simple(null, null));
        }

        [Test()]
        public void test_empty() {
            Assert.AreEqual("", service.add_simple("", ""));
        }

        [Test()]
        public void test() {
            Assert.AreEqual(
                "hello world", service.add_simple("hello ", "world"));
        }
    }
}
