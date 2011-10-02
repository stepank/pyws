<?
require_once 'base.php';

class GetTestCase extends TestServiceTestCase {

    public function test_null_ret() {
        $r = $this->service->get_tree(0);
        $this->assertEquals($r, null);
    }

    public function test_notset() {
        $r = $this->service->get_tree(1);
        $this->assertEquals($r->value, 1);
        $this->assertEquals($r->left, null);
        $this->assertEquals($r->right, null);
    }

    public function test_null() {
        $r = $this->service->get_tree(2);
        $this->assertEquals($r->value, 2);
        $this->assertEquals($r->left, null);
        $this->assertEquals($r->right, null);
    }

    public function test() {
        $r = $this->service->get_tree(3);
        $this->assertEquals($r->value, 3);
        $this->assertEquals($r->left->value, 4);
        $this->assertEquals($r->left->left, null);
        $this->assertEquals($r->left->right, null);
        $this->assertEquals($r->right->value, 5);
        $this->assertEquals($r->right->left, null);
        $this->assertEquals($r->right->right, null);
    }
}
