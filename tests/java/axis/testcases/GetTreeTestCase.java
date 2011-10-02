package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.Tree;
import com.example.types.ABStringDict;

public class GetTreeTestCase extends TestServiceTestCase {

    @Test
    public void test_null_ret() {
        try {
            Tree r = port.get_tree(0);
            Assert.assertTrue(r == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_notset() {
        try {
            Tree r = port.get_tree(1);
            Assert.assertTrue(r.getValue() == 1);
            Assert.assertTrue(r.getLeft() == null);
            Assert.assertTrue(r.getRight() == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_null() {
        try {
            Tree r = port.get_tree(2);
            Assert.assertTrue(r.getValue() == 2);
            Assert.assertTrue(r.getLeft() == null);
            Assert.assertTrue(r.getRight() == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        try {
            Tree r = port.get_tree(3);
            Assert.assertTrue(r.getValue() == 3);
            Assert.assertTrue(r.getLeft().getValue() == 4);
            Assert.assertTrue(r.getLeft().getLeft() == null);
            Assert.assertTrue(r.getLeft().getRight() == null);
            Assert.assertTrue(r.getRight().getValue() == 5);
            Assert.assertTrue(r.getRight().getLeft() == null);
            Assert.assertTrue(r.getRight().getRight() == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
