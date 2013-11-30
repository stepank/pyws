package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddFloatsTestCase extends TestServiceTestCase {

    @Test
    public void test() throws Exception {
        Assert.assertEquals(
            (float)15.8, port.add_floats((float)10.5, (float)5.3), 0.01);
    }
}
