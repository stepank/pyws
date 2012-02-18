using System;
using NUnit.Framework;

namespace TestCases {

    [TestFixture()]
    public class NeedsAuthTest : TestServiceTest {

        [Test()]
        public void test() {
            Headers headers = new Headers();
            headers.username = "user";
            headers.password = "pass";
            service.HeadersValue = headers;
            Assert.AreEqual("hello user", service.say_hello());
        }

        [Test()]
        public void test_exception() {
            Headers headers = new Headers();
            headers.username = "fake";
            headers.password = "pass";
            service.HeadersValue = headers;
            try {
                service.say_hello();
            } catch(Exception e) {
                Assert.AreEqual("Access denied for user fake", e.Message);
                return;
            }
            Assert.True(false, "Exception hasn't been thrown");
        }
    }
}
