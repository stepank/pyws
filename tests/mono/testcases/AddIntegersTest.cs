using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddIntegersTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual(service.add_integers(null, null), 0);
        }

        [Test()]
        public void test_empty() {
            Assert.AreEqual(service.add_integers(0, 0), 0);
        }

        [Test()]
        public void test() {
            Assert.AreEqual(service.add_integers(100, 50), 150);
        }
    }
}
