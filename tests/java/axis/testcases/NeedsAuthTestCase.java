package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.TestBindingStub;
import com.example.types.Headers;

public class NeedsAuthTestCase extends TestServiceTestCase {

    @Test
    public void test() throws Exception {
        TestBindingStub stub = (TestBindingStub)port;
        stub.setHeader(
            "http://example.com/", "headers",
            (new Headers("user", "pass")));
        Assert.assertEquals("hello user", port.say_hello());
    }

    @Test
    public void test_exception() throws Exception {
        TestBindingStub stub = (TestBindingStub)port;
        stub.setHeader("http://example.com/", "headers",
            (new Headers("fake", "pass")));
        try {
            port.say_hello();
        } catch (com.example.types.Error e) {
            Assert.assertTrue(
                e.toString().equals("Access denied for user fake"));
            return;
        }
        Assert.assertTrue("Exception hasn't been thrown", false);
    }
}
