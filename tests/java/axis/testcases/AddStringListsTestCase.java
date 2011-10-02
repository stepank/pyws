package testcases;

import org.junit.Test;
import org.junit.Assert;

public class AddStringListsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() {
        try {
            java.lang.String[] r = port.add_string_lists(null, null);
            Assert.assertTrue(r.length == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty() {
        try {
            java.lang.String[] a1 = {};
            java.lang.String[] a2 = {};
            java.lang.String[] r = port.add_string_lists(a1, a2);
            Assert.assertTrue(r.length == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_null_value() {
        try {
            java.lang.String[] a1 = {null};
            java.lang.String[] a2 = {null};
            java.lang.String[] r = port.add_string_lists(a1, a2);
            Assert.assertTrue(r.length == 1);
            Assert.assertTrue(r[0].equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty_value() {
        try {
            java.lang.String[] a1 = {""};
            java.lang.String[] a2 = {""};
            java.lang.String[] r = port.add_string_lists(a1, a2);
            Assert.assertTrue(r.length == 1);
            Assert.assertTrue(r[0].equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_equal_size() {
        try {
            java.lang.String[] a1 = {"a", "b", "c"};
            java.lang.String[] a2 = {"d", "e", "f"};
            java.lang.String[] r = port.add_string_lists(a1, a2);
            Assert.assertTrue(r.length == 3);
            Assert.assertTrue(r[0].equals("ad"));
            Assert.assertTrue(r[1].equals("be"));
            Assert.assertTrue(r[2].equals("cf"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_diff_size() {
        try {
            java.lang.String[] a1 = {"a", "b", "c"};
            java.lang.String[] a2 = {"d", "e", "f", "g", "h"};
            java.lang.String[] r = port.add_string_lists(a1, a2);
            Assert.assertTrue(r.length == 5);
            Assert.assertTrue(r[0].equals("ad"));
            Assert.assertTrue(r[1].equals("be"));
            Assert.assertTrue(r[2].equals("cf"));
            Assert.assertTrue(r[3].equals("g"));
            Assert.assertTrue(r[4].equals("h"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
