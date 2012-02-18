using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class AddFloatsTest : TestServiceTest {

        [Test()]
        public void test_null() {
            Assert.AreEqual(service.add_floats(null, null), 0);
        }

        [Test()]
        public void test_empty() {
            Assert.AreEqual(service.add_floats(0, 0), 0);
        }

        [Test()]
        public void test() {
            Assert.AreEqual(
                service.add_floats((float)10.5, (float)5.3), (float)15.8);
        }
    }
}
