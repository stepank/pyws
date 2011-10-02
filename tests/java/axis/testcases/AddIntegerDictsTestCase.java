package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.ABIntegerDict;

public class AddIntegerDictsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() {
        try {
            ABIntegerDict r = port.add_integer_dicts(null, null);
            Assert.assertTrue(r.getA() == 0);
            Assert.assertTrue(r.getB() == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_notset() {
        try {
            ABIntegerDict p = new ABIntegerDict();
            ABIntegerDict q = new ABIntegerDict();
            ABIntegerDict r = port.add_integer_dicts(p, q);
            Assert.assertTrue(r.getA() == 0);
            Assert.assertTrue(r.getB() == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_null() {
        try {
            ABIntegerDict p = new ABIntegerDict(null, null);
            ABIntegerDict q = new ABIntegerDict(null, null);
            ABIntegerDict r = port.add_integer_dicts(p, q);
            Assert.assertTrue(r.getA() == 0);
            Assert.assertTrue(r.getB() == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty() {
        try {
            ABIntegerDict p = new ABIntegerDict(0, 0);
            ABIntegerDict q = new ABIntegerDict(0, 0);
            ABIntegerDict r = port.add_integer_dicts(p, q);
            Assert.assertTrue(r.getA() == 0);
            Assert.assertTrue(r.getB() == 0);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        try {
            ABIntegerDict p = new ABIntegerDict(100, 50);
            ABIntegerDict q = new ABIntegerDict(50, 25);
            ABIntegerDict r = port.add_integer_dicts(p, q);
            Assert.assertTrue(r.getA() == 150);
            Assert.assertTrue(r.getB() == 75);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
