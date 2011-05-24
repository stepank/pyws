package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddFloatsTestCase extends TestServiceTestCase {

    @Test
    public void add_floats() {
        try {
            Assert.assertTrue(port.add_floats(100, 50) == 150);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}