package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddSimpleTestCase extends TestServiceTestCase {

    @Test
    public void test_null() {
        try {
            Assert.assertTrue(port.add_simple(null, null).equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty() {
        try {
            Assert.assertTrue(port.add_simple("", "").equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        try {
            Assert.assertTrue(
                port.add_simple("hello", " world").equals("hello world"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
