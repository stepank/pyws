using System;
using NUnit.Framework;

namespace TestCases {

    public class TestServiceTest {

        public TestService service;

        [SetUp]
        public void SetUp() {
            service = new TestService();
        }
    }
}
