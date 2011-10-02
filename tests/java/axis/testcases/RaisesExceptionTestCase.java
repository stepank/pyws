package testcases;

import java.rmi.RemoteException;

import org.junit.Test;
import org.junit.Assert;

public class RaisesExceptionTestCase extends TestServiceTestCase {

    @Test
    public void test() {
        try {
            System.out.println(port.raises_exception());
        } catch (com.example.types.Error e) {
            Assert.assertTrue(e.toString().equals("hello error"));
            return;
        } catch (RemoteException e) {}
        Assert.assertTrue("Exception hasn't been thrown", false);
    }
}
