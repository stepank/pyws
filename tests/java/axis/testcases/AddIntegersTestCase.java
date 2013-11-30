package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddIntegersTestCase extends TestServiceTestCase {

    @Test
    public void test() throws Exception {
        Assert.assertEquals(150, port.add_integers(100, 50));
    }
}
