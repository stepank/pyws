<?
require_once 'base.php';

class AddSimpleTestCase extends TestServiceTestCase {

    public function test_null() {
        $this->assertEquals($this->service->add_simple(null, null), '');
    }

    public function test_empty() {
        $this->assertEquals($this->service->add_simple('', ''), '');
    }

    public function test() {
        $this->assertEquals(
            $this->service->add_simple('hello', ' world'), 'hello world');
    }
}
