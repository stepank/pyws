using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class RaisesExceptionTest : TestServiceTest {

        [Test()]
        public void test_null() {
            try {
                service.raises_exception();
            } catch(Exception e) {
                Assert.AreEqual("hello error", e.Message);
                return;
            }
            Assert.True(false, "Exception hasn't been thrown");
        }
    }
}
