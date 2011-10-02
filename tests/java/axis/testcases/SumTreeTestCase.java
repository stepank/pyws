package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.Tree;

public class SumTreeTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() {
        try {
            java.lang.Integer r = port.sum_tree(null);
            Assert.assertTrue(r == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_notset() {
        try {
            java.lang.Integer r = port.sum_tree(new Tree());
            Assert.assertTrue(r == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_null() {
        try {
            java.lang.Integer r = port.sum_tree(new Tree(null, null, null));
            Assert.assertTrue(r == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_value() {
        try {
            java.lang.Integer r = port.sum_tree(new Tree(10, null, null));
            Assert.assertTrue(r == 10);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        try {
            java.lang.Integer r = port.sum_tree(new Tree(10,
                new Tree(20, null, null),
                new Tree(30, null, null)
            ));
            Assert.assertTrue(r == 60);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
