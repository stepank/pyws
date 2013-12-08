package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddIntegerListsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() throws Exception {
        int[] r = port.add_integer_lists(null, null);
        Assert.assertEquals(0, r.length);
    }

    @Test
    public void test_empty() throws Exception {
        int[] a1 = {};
        int[] a2 = {};
        int[] r = port.add_integer_lists(a1, a2);
        Assert.assertEquals(0, r.length);
    }

    @Test
    public void test_empty_value() throws Exception {
        int[] a1 = {0};
        int[] a2 = {0};
        int[] r = port.add_integer_lists(a1, a2);
        Assert.assertEquals(1, r.length);
        Assert.assertEquals(0, r[0]);
    }

    @Test
    public void test_equal_size() throws Exception {
        int[] a1 = {1, 2, 3};
        int[] a2 = {3, -5, 0};
        int[] r = port.add_integer_lists(a1, a2);
        Assert.assertEquals(3, r.length);
        Assert.assertEquals(4, r[0]);
        Assert.assertEquals(-3, r[1]);
        Assert.assertEquals(3, r[2]);
    }

    @Test
    public void test_diff_size() throws Exception {
        int[] a1 = {1, 2, 3};
        int[] a2 = {3, -5, 0, 11, -5};
        int[] r = port.add_integer_lists(a1, a2);
        Assert.assertEquals(5, r.length);
        Assert.assertEquals(4, r[0]);
        Assert.assertEquals(-3, r[1]);
        Assert.assertEquals(3, r[2]);
        Assert.assertEquals(11, r[3]);
        Assert.assertEquals(-5, r[4]);
    }
}
