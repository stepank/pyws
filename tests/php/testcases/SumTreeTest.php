<?
require_once 'base.php';

class SumTreeTestCase extends TestServiceTestCase {

    public function test_notset() {
        $p = new Tree();
        $r = $this->service->sum_tree($p);
        $this->assertEquals($r, 0);
    }

    public function test_null() {
        $p = new Tree();
        $p->value = null;
        $p->left = null;
        $p->right = null;
        $r = $this->service->sum_tree($p);
        $this->assertEquals($r, 0);
    }

    public function test_value() {
        $p = new Tree();
        $p->value = 10;
        $p->left = null;
        $p->right = null;
        $r = $this->service->sum_tree($p);
        $this->assertEquals($r, 10);
    }

    public function test() {
        $p = new Tree();
        $p->value = 10;
        $p->left = new Tree();
        $p->left->value = 20;
        $p->right = new Tree();
        $p->right->value = 30;
        $r = $this->service->sum_tree($p);
        $this->assertEquals($r, 60);
    }
}
