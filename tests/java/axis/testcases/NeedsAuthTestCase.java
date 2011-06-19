package testcases;

import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

import com.example.TestBindingStub;
import com.example.types.Headers;

public class NeedsAuthTestCase extends TestServiceTestCase {

    @Before
    public void setUp() {
        super.setUp();
        TestBindingStub stub = (TestBindingStub)port;
        stub.setHeader("http://example.com/", "headers",
            (Object)(new Headers("user", "pass")));
    }

    @Test
    public void needs_auth() {
        try {
            Assert.assertTrue(
                port.needs_auth("hello", " world").equals("hello world"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}