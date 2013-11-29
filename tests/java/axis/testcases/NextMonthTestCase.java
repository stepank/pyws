package testcases;

import java.util.Calendar;
import java.util.Date;

import org.junit.Assert;
import org.junit.Test;

public class NextMonthTestCase extends TestServiceTestCase {

    @Test
    public void test_null() throws Exception {
        Assert.assertEquals(null, port.next_month(null));
    }

    @Test
    public void test() throws Exception {
        Assert.assertEquals(
            new Date(2013, 9, 11), port.next_month(new Date(2013, 8, 11)));
    }

    @Test
    public void test_dt_null() throws Exception {
        Assert.assertEquals(null, port.next_month_dt(null));
    }

    @Test
    public void test_dt() throws Exception {
        Calendar origin = Calendar.getInstance();
        origin.setTime(new Date(1313826085123L));
        Assert.assertEquals(
            new Date(1316504485123L), port.next_month_dt(origin).getTime());
    }
}
