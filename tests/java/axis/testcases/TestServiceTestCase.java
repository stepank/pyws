package testcases;

import org.junit.Before;
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
}