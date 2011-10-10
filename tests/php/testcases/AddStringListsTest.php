<?
require_once 'base.php';

class AddStringListsTestCase extends TestServiceTestCase {

    public function test_notset() {
        $p = new StringList();
        $q = new StringList();
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_null() {
        $p = new StringList();
        $p->item = null;
        $q = new StringList();
        $q->item = null;
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_empty() {
        $p = new StringList();
        $p->item = array();
        $q = new StringList();
        $q->item = array();
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 0);
    }

    public function test_null_value() {
        $p = new StringList();
        $p->item = array(null);
        $q = new StringList();
        $q->item = array(null);
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 1);
        $this->assertEquals($r->item, '');
        # Warning: as there only one element in the returned list,
        # SoapClient interprets it not as an array.
    }

    public function test_empty_value() {
        $p = new StringList();
        $p->item = array('');
        $q = new StringList();
        $q->item = array('');
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 1);
        $this->assertEquals($r->item, '');
        # Warning: as there only one element in the returned list,
        # SoapClient interprets it not as an array.
    }

    public function test_equal_size() {
        $p = new StringList();
        $p->item = array('a', 'b', 'c');
        $q = new StringList();
        $q->item = array('d', 'e', 'f');
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 3);
        $this->assertEquals($r->item[0], 'ad');
        $this->assertEquals($r->item[1], 'be');
        $this->assertEquals($r->item[2], 'cf');
    }

    public function test_diff_size() {
        $p = new StringList();
        $p->item = array('a', 'b', 'c');
        $q = new StringList();
        $q->item = array('d', 'e', 'f', 'g', 'h');
        $r = $this->service->add_string_lists($p, $q);
        $this->assertEquals(count($r->item), 5);
        $this->assertEquals($r->item[0], 'ad');
        $this->assertEquals($r->item[1], 'be');
        $this->assertEquals($r->item[2], 'cf');
        $this->assertEquals($r->item[3], 'g');
        $this->assertEquals($r->item[4], 'h');
    }
}
