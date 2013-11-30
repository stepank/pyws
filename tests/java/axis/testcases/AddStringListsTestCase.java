package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddStringListsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() throws Exception {
        java.lang.String[] r = port.add_string_lists(null, null);
        Assert.assertEquals(0, r.length);
    }

    @Test
    public void test_empty() throws Exception {
        java.lang.String[] a1 = {};
        java.lang.String[] a2 = {};
        java.lang.String[] r = port.add_string_lists(a1, a2);
        Assert.assertEquals(0, r.length);
    }

    @Test
    public void test_null_value() throws Exception {
        java.lang.String[] a1 = {null};
        java.lang.String[] a2 = {null};
        java.lang.String[] r = port.add_string_lists(a1, a2);
        Assert.assertEquals(1, r.length);
        Assert.assertEquals("", r[0]);
    }

    @Test
    public void test_empty_value() throws Exception {
        java.lang.String[] a1 = {""};
        java.lang.String[] a2 = {""};
        java.lang.String[] r = port.add_string_lists(a1, a2);
        Assert.assertEquals(1, r.length);
        Assert.assertEquals("", r[0]);
    }

    @Test
    public void test_equal_size() throws Exception {
        java.lang.String[] a1 = {"a", "b", "c"};
        java.lang.String[] a2 = {"d", "e", "f"};
        java.lang.String[] r = port.add_string_lists(a1, a2);
        Assert.assertEquals(3, r.length);
        Assert.assertEquals("ad", r[0]);
        Assert.assertEquals("be", r[1]);
        Assert.assertEquals("cf", r[2]);
    }

    @Test
    public void test_diff_size() throws Exception {
        java.lang.String[] a1 = {"a", "b", "c"};
        java.lang.String[] a2 = {"d", "e", "f", "g", "h"};
        java.lang.String[] r = port.add_string_lists(a1, a2);
        Assert.assertEquals(5, r.length);
        Assert.assertEquals("ad", r[0]);
        Assert.assertEquals("be", r[1]);
        Assert.assertEquals("cf", r[2]);
        Assert.assertEquals("g", r[3]);
        Assert.assertEquals("h", r[4]);
    }
}
