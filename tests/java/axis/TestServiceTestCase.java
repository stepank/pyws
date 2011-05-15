import org.junit.Test;
import org.junit.Before;
import org.junit.Assert;
import com.example.TestService;
import com.example.TestServiceLocator;
import com.example.TestPortType;

public class TestServiceTestCase {

    public TestService service;
    public TestPortType port;

    @Before
    public void setUp() {
        service = new TestServiceLocator();
        try {
            port = service.getTestPort();
        } catch (javax.xml.rpc.ServiceException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void simple() {
        try {
            Assert.assertTrue(port.simple("hello").equals("hello world"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void add_integer() {
        try {
            Assert.assertTrue(port.add_integer(100, 50) == 150);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void add_float() {
        try {
            Assert.assertTrue(port.add_float(100, 50) == 150.0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}