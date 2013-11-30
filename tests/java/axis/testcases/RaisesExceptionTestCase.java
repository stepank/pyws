package testcases;

import java.rmi.RemoteException;

import org.junit.Test;
import org.junit.Assert;

public class RaisesExceptionTestCase extends TestServiceTestCase {

    @Test
    public void test() throws Exception {
        try {
            System.out.println(port.raises_exception("hello"));
        } catch (com.example.types.Error e) {
            Assert.assertTrue(e.toString().equals("hello error"));
            return;
        }
        Assert.assertTrue("Exception hasn't been thrown", false);
    }
}
