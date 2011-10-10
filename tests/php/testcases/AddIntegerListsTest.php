<?
require_once 'base.php';

class AddIntegerListsTestCase extends TestServiceTestCase {

    public function test_notset() {
        $p = new IntegerList();
        $q = new IntegerList();
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_null() {
        $p = new IntegerList();
        $p->item = null;
        $q = new IntegerList();
        $q->item = null;
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_empty() {
        $p = new IntegerList();
        $p->item = array();
        $q = new IntegerList();
        $q->item = array();
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_null_value() {
        $p = new IntegerList();
        $p->item = array(null);
        $q = new IntegerList();
        $q->item = array(null);
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 1);
        $this->assertEquals($r->item, 0);
        # Warning: as there only one element in the returned list,
        # SoapClient interprets it not as an array.
    }

    public function test_empty_value() {
        $p = new IntegerList();
        $p->item = array(0);
        $q = new IntegerList();
        $q->item = array(0);
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 1);
        $this->assertEquals($r->item, 0);
        # Warning: as there only one element in the returned list,
        # SoapClient interprets it not as an array.
    }

    public function test_equal_size() {
        $p = new IntegerList();
        $p->item = array(1, 2, 3);
        $q = new IntegerList();
        $q->item = array(3, -5, 0);
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 3);
        $this->assertEquals($r->item[0], 4);
        $this->assertEquals($r->item[1], -3);
        $this->assertEquals($r->item[2], 3);
    }

    public function test_diff_size() {
        $p = new IntegerList();
        $p->item = array(1, 2, 3);
        $q = new IntegerList();
        $q->item = array(3, -5, 0, 11, -5);
        $r = $this->service->add_integer_lists($p, $q);
        $this->assertEquals(count($r->item), 5);
        $this->assertEquals($r->item[0], 4);
        $this->assertEquals($r->item[1], -3);
        $this->assertEquals($r->item[2], 3);
        $this->assertEquals($r->item[3], 11);
        $this->assertEquals($r->item[4], -5);
    }
}
