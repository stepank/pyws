<?
require_once 'base.php';

class AddStringDictsTestCase extends TestServiceTestCase {

    public function test_notset() {
        $p = new ABStringDict();
        $q = new ABStringDict();
        $r = $this->service->add_string_dicts($p, $q);
        $this->assertEquals($r->a, '');
        $this->assertEquals($r->b, '');
    }

    public function test_null() {
        $p = new ABStringDict();
        $p->a = null;
        $p->b = null;
        $q = new ABStringDict();
        $q->a = null;
        $q->b = null;
        $r = $this->service->add_string_dicts($p, $q);
        $this->assertEquals($r->a, '');
        $this->assertEquals($r->b, '');
    }

    public function test_empty() {
        $p = new ABStringDict();
        $p->a = '';
        $p->b = '';
        $q = new ABStringDict();
        $q->a = '';
        $q->b = '';
        $r = $this->service->add_string_dicts($p, $q);
        $this->assertEquals($r->a, '');
        $this->assertEquals($r->b, '');
    }

    public function test() {
        $p = new ABStringDict();
        $p->a = 'hello';
        $p->b = 'say';
        $q = new ABStringDict();
        $q->a = ' world';
        $q->b = ' hello';
        $r = $this->service->add_string_dicts($p, $q);
        $this->assertEquals($r->a, 'hello world');
        $this->assertEquals($r->b, 'say hello');
    }
}
