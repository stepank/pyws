package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddFloatsTestCase extends TestServiceTestCase {

    @Test
    public void test() {
        try {
            Assert.assertTrue(
                port.add_floats((float)10.5, (float)5.3) == (float)15.8);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
