package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.ABStringDict;

public class AddStringDictsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() throws Exception {
        ABStringDict r = port.add_string_dicts(null, null);
        Assert.assertEquals("", r.getA());
        Assert.assertEquals("", r.getB());
    }

    @Test
    public void test_notset() throws Exception {
        ABStringDict p = new ABStringDict();
        ABStringDict q = new ABStringDict();
        ABStringDict r = port.add_string_dicts(p, q);
        Assert.assertEquals("", r.getA());
        Assert.assertEquals("", r.getB());
    }

    @Test
    public void test_null() throws Exception {
        ABStringDict p = new ABStringDict(null, null);
        ABStringDict q = new ABStringDict(null, null);
        ABStringDict r = port.add_string_dicts(p, q);
        Assert.assertEquals("", r.getA());
        Assert.assertEquals("", r.getB());
    }

    @Test
    public void test_empty() throws Exception {
        ABStringDict p = new ABStringDict("", "");
        ABStringDict q = new ABStringDict("", "");
        ABStringDict r = port.add_string_dicts(p, q);
        Assert.assertEquals("", r.getA());
        Assert.assertEquals("", r.getB());
    }

    @Test
    public void test() throws Exception {
        ABStringDict p = new ABStringDict("hello", "say");
        ABStringDict q = new ABStringDict(" world", " hello");
        ABStringDict r = port.add_string_dicts(p, q);
        Assert.assertEquals("hello world", r.getA());
        Assert.assertEquals("say hello", r.getB());
    }
}
