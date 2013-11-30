package testcases;

import org.junit.Test;
import org.junit.Assert;

public class FlipBoolTestCase extends TestServiceTestCase {

    @Test
    public void test() throws Exception {
        Assert.assertEquals(false, port.flip_boolean(true));
        Assert.assertEquals(true, port.flip_boolean(false));
    }
}
