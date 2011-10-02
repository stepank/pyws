<?
require_once 'base.php';

class NextMonthTestCase extends TestServiceTestCase {

    public function test_null() {
        $this->assertEquals($this->service->next_month(null), null);
    }

    public function test() {
        $this->assertEquals(
            $this->service->next_month('2011-08-20'),
            '2011-09-20');
    }

    public function test_dt_null() {
        $this->assertEquals($this->service->next_month_dt(null), null);
    }

    public function test_dt() {
        $this->assertEquals(
            $this->service->next_month_dt('2011-08-20T00:04:59Z'),
            '2011-09-20T00:04:59Z');
    }
}
