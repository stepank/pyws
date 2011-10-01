package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.TestBindingStub;
import com.example.types.Headers;

public class NeedsAuthTestCase extends TestServiceTestCase {

    @Test
    public void needs_context() {
        com.example.TestBindingStub stub = (com.example.TestBindingStub)port;
        stub.setHeader("http://example.com/", "headers",
            (Object)(new com.example.types.Headers("user", "pass")));
        try {
            Assert.assertTrue(
                port.say_hello().equals("hello user"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void needs_context_exception() {
        com.example.TestBindingStub stub = (com.example.TestBindingStub)port;
        stub.setHeader("http://example.com/", "headers",
            (Object)(new com.example.types.Headers("fake", "pass")));
        try {
            port.say_hello();
        } catch (com.example.types.Error e) {
            Assert.assertTrue(
                e.toString().equals("Access denied for user fake"));
            return;
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
        Assert.assertTrue("Exception hasn't been thrown", false);
    }
}
