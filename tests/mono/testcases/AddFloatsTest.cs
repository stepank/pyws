using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddFloatsTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual(0, service.add_floats(null, null));
        }

        [Test()]
        public void test_empty() {
            Assert.AreEqual(0, service.add_floats(0, 0));
        }

        [Test()]
        public void test() {
            Assert.AreEqual(
                (float)15.8, service.add_floats((float)10.5, (float)5.3));
        }
    }
}
