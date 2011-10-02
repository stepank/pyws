package testcases;

import java.util.Calendar;
import java.util.Date;

import org.junit.Assert;
import org.junit.Test;

public class NextMonthTestCase extends TestServiceTestCase {

    @Test
    public void test_null() {
        try {
            //noinspection NullableProblems
            Assert.assertTrue(port.next_month(null) == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test() {
        Date d = new Date(1313784000000L);
        try {
            Assert.assertTrue(port.next_month(d).getTime() == 1316462400000L);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_dt_null() {
        try {
            //noinspection NullableProblems
            Assert.assertTrue(port.next_month_dt(null) == null);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }

    @Test
    public void test_dt() {
        Calendar d = Calendar.getInstance();
        d.setTime(new Date(1313826085000L));
        try {
            Assert.assertTrue(
                port.next_month_dt(d).getTime().getTime() == 1316504485000L);
        } catch (java.rmi.RemoteException e) {
            System.out.println("Exception: " + e.toString());
        }
    }
}
