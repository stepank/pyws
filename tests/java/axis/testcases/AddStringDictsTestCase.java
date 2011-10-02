package testcases;

import org.junit.Test;
import org.junit.Assert;

import com.example.types.ABStringDict;

public class AddStringDictsTestCase extends TestServiceTestCase {

    @Test
    public void test_null_args() {
        try {
            ABStringDict r = port.add_string_dicts(null, null);
            Assert.assertTrue(r.getA().equals(""));
            Assert.assertTrue(r.getB().equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_notset() {
        try {
            ABStringDict p = new ABStringDict();
            ABStringDict q = new ABStringDict();
            ABStringDict r = port.add_string_dicts(p, q);
            Assert.assertTrue(r.getA().equals(""));
            Assert.assertTrue(r.getB().equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_null() {
        try {
            ABStringDict p = new ABStringDict(null, null);
            ABStringDict q = new ABStringDict(null, null);
            ABStringDict r = port.add_string_dicts(p, q);
            Assert.assertTrue(r.getA().equals(""));
            Assert.assertTrue(r.getB().equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_empty() {
        try {
            ABStringDict p = new ABStringDict("", "");
            ABStringDict q = new ABStringDict("", "");
            ABStringDict r = port.add_string_dicts(p, q);
            Assert.assertTrue(r.getA().equals(""));
            Assert.assertTrue(r.getB().equals(""));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        try {
            ABStringDict p = new ABStringDict("hello", "say");
            ABStringDict q = new ABStringDict(" world", " hello");
            ABStringDict r = port.add_string_dicts(p, q);
            Assert.assertTrue(r.getA().equals("hello world"));
            Assert.assertTrue(r.getB().equals("say hello"));
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
