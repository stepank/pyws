package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddSimpleTestCase extends TestServiceTestCase {

    @Test
    public void test_null() throws Exception {
        Assert.assertEquals("", port.add_simple(null, null));
    }

    @Test
    public void test_empty() throws Exception {
        Assert.assertEquals("", port.add_simple("", ""));
    }

    @Test
    public void test() throws Exception {
        Assert.assertEquals("hello world", port.add_simple("hello", " world"));
    }
}
