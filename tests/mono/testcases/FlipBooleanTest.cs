using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class FlipBoolTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual(true, service.flip_boolean(null));
        }

        [Test()]
        public void test() {
            Assert.AreEqual(true, service.flip_boolean(false));
            Assert.AreEqual(false, service.flip_boolean(true));
        }
    }
}