package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddSimpleTestCase extends TestServiceTestCase {

    @Test
    public void add_simple_null() {
        try {
            Assert.assertTrue(port.add_simple(null, null).equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void add_simple_empty() {
        try {
            Assert.assertTrue(port.add_simple("", "").equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void add_simple() {
        try {
            Assert.assertTrue(
                port.add_simple("hello", " world").equals("hello world"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}