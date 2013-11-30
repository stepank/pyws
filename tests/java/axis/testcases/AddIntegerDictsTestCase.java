package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.ABIntegerDict;

public class AddIntegerDictsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() throws Exception {
        ABIntegerDict r = port.add_integer_dicts(null, null);
        Assert.assertEquals((long)0, (long)r.getA());
        Assert.assertEquals((long)0, (long)r.getB());
    }

    @Test
    public void test_notset() throws Exception {
        ABIntegerDict p = new ABIntegerDict();
        ABIntegerDict q = new ABIntegerDict();
        ABIntegerDict r = port.add_integer_dicts(p, q);
        Assert.assertEquals((long)0, (long)r.getA());
        Assert.assertEquals((long)0, (long)r.getB());
    }

    @Test
    public void test_null() throws Exception {
        ABIntegerDict p = new ABIntegerDict(null, null);
        ABIntegerDict q = new ABIntegerDict(null, null);
        ABIntegerDict r = port.add_integer_dicts(p, q);
        Assert.assertEquals((long)0, (long)r.getA());
        Assert.assertEquals((long)0, (long)r.getB());
    }

    @Test
    public void test_empty() throws Exception {
        ABIntegerDict p = new ABIntegerDict(0, 0);
        ABIntegerDict q = new ABIntegerDict(0, 0);
        ABIntegerDict r = port.add_integer_dicts(p, q);
        Assert.assertEquals((long)0, (long)r.getA());
        Assert.assertEquals((long)0, (long)r.getB());
    }

    @Test
    public void test() throws Exception {
        ABIntegerDict p = new ABIntegerDict(100, 50);
        ABIntegerDict q = new ABIntegerDict(50, 25);
        ABIntegerDict r = port.add_integer_dicts(p, q);
        Assert.assertEquals((long)150, (long)r.getA());
        Assert.assertEquals((long)75, (long)r.getB());
    }
}
