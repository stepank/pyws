package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddIntegerListsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() {
        try {
            int[] r = port.add_integer_lists(null, null);
            Assert.assertTrue(r.length == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty() {
        try {
            int[] a1 = {};
            int[] a2 = {};
            int[] r = port.add_integer_lists(a1, a2);
            Assert.assertTrue(r.length == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty_value() {
        try {
            int[] a1 = {0};
            int[] a2 = {0};
            int[] r = port.add_integer_lists(a1, a2);
            Assert.assertTrue(r.length == 1);
            Assert.assertTrue(r[0] == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_equal_size() {
        try {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0};
            int[] r = port.add_integer_lists(a1, a2);
            Assert.assertTrue(r.length == 3);
            Assert.assertTrue(r[0] == 4);
            Assert.assertTrue(r[1] == -3);
            Assert.assertTrue(r[2] == 3);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_diff_size() {
        try {
            int[] a1 = {1, 2, 3};
            int[] a2 = {3, -5, 0, 11, -5};
            int[] r = port.add_integer_lists(a1, a2);
            Assert.assertTrue(r.length == 5);
            Assert.assertTrue(r[0] == 4);
            Assert.assertTrue(r[1] == -3);
            Assert.assertTrue(r[2] == 3);
            Assert.assertTrue(r[3] == 11);
            Assert.assertTrue(r[4] == -5);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
