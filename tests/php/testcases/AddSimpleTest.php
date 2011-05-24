<?
require_once 'base.php';

class AddSimpleTestCase extends TestServiceTestCase {

    public function test_add_simple_null() {
        $this->assertEquals($this->service->add_simple(null, null), '');
    }

    public function test_add_simple_empty() {
        $this->assertEquals($this->service->add_simple('', ''), '');
    }

    public function test_add_simple() {
        $this->assertEquals(
            $this->service->add_simple('hello', ' world'), 'hello world');
    }
}
