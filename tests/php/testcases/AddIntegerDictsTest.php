<?
require_once 'base.php';

class AddIntegerDictsTestCase extends TestServiceTestCase {

    public function test_notset() {
        $p = new ABIntegerDict();
        $q = new ABIntegerDict();
        $r = $this->service->add_integer_dicts($p, $q);
        $this->assertEquals($r->a, 0);
        $this->assertEquals($r->b, 0);
    }

    public function test_null() {
        $p = new ABIntegerDict();
        $p->a = null;
        $p->b = null;
        $q = new ABIntegerDict();
        $q->a = null;
        $q->b = null;
        $r = $this->service->add_integer_dicts($p, $q);
        $this->assertEquals($r->a, 0);
        $this->assertEquals($r->b, 0);
    }

    public function test_empty() {
        $p = new ABIntegerDict();
        $p->a = 0;
        $p->b = 0;
        $q = new ABIntegerDict();
        $q->a = 0;
        $q->b = 0;
        $r = $this->service->add_integer_dicts($p, $q);
        $this->assertEquals($r->a, 0);
        $this->assertEquals($r->b, 0);
    }

    public function test() {
        $p = new ABIntegerDict();
        $p->a = 100;
        $p->b = 50;
        $q = new ABIntegerDict();
        $q->a = 50;
        $q->b = 25;
        $r = $this->service->add_integer_dicts($p, $q);
        $this->assertEquals($r->a, 150);
        $this->assertEquals($r->b, 75);
    }
}
