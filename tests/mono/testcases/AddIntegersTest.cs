using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddIntegersTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual(0, service.add_integers(null, null));
        }

        [Test()]
        public void test_empty() {
            Assert.AreEqual(0, service.add_integers(0, 0));
        }

        [Test()]
        public void test() {
            Assert.AreEqual(150, service.add_integers(100, 50));
        }
    }
}
