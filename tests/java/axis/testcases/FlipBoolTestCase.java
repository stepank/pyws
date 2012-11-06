package testcases;

import org.junit.Test;
import org.junit.Assert;

public class FlipBoolTestCase extends TestServiceTestCase {

    @Test
    public void test() {
        try {
            Assert.assertTrue(port.flip_boolean(true) == false);
            Assert.assertTrue(port.flip_boolean(false) == true);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
