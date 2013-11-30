package testcases;

import org.junit.Before;
import com.example.TestService;
import com.example.TestServiceLocator;
import com.example.TestPortType;

public class TestServiceTestCase {

    public TestService service;
    public TestPortType port;

    @Before
    public void setUp() throws Exception {
        service = new TestServiceLocator();
        port = service.getTestPort();
    }
}