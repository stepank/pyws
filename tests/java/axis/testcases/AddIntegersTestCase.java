package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddIntegersTestCase extends TestServiceTestCase {

    @Test
    public void test() {
        try {
            Assert.assertTrue(port.add_integers(100, 50) == 150);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
