package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.Tree;

public class SumTreeTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() throws Exception {
        Assert.assertEquals((long)0, (long)port.sum_tree(null));
    }

    @Test
    public void test_notset() throws Exception {
        Assert.assertEquals((long)0, (long)port.sum_tree(new Tree()));
    }

    @Test
    public void test_null() throws Exception {
        Assert.assertEquals(
            (long)0, (long)port.sum_tree(new Tree(null, null, null)));
    }

    @Test
    public void test_value() throws Exception {
        Assert.assertEquals(
            (long)10, (long)port.sum_tree(new Tree(10, null, null)));
    }

    @Test
    public void test() throws Exception {
        Assert.assertEquals(
            (long)60, (long)port.sum_tree(new Tree(10,
                new Tree(20, null, null),
                new Tree(30, null, null)
            ))
        );
    }
}
