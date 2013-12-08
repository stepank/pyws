package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.Tree;
import com.example.types.ABStringDict;

public class GetTreeTestCase extends TestServiceTestCase {

    @Test
    public void test_null_ret() throws Exception {
        Tree r = port.get_tree(0);
        Assert.assertEquals(null, r);
    }

    @Test
    public void test_notset() throws Exception {
        Tree r = port.get_tree(1);
        Assert.assertEquals((long)1, (long)r.getValue());
        Assert.assertEquals(null, r.getLeft());
        Assert.assertEquals(null, r.getRight());
    }

    @Test
    public void test_null() throws Exception {
        Tree r = port.get_tree(2);
        Assert.assertEquals((long)2, (long)r.getValue());
        Assert.assertEquals(null, r.getLeft());
        Assert.assertEquals(null, r.getRight());
    }

    @Test
    public void test() throws Exception {
        Tree r = port.get_tree(3);
        Assert.assertEquals((long)3, (long)r.getValue());
        Assert.assertEquals((long)4, (long)r.getLeft().getValue());
        Assert.assertEquals(null, r.getLeft().getLeft());
        Assert.assertEquals(null, r.getLeft().getRight());
        Assert.assertEquals((long)5, (long)r.getRight().getValue());
        Assert.assertEquals(null, r.getRight().getLeft());
        Assert.assertEquals(null, r.getRight().getRight());
    }
}
