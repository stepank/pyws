<?
require_once 'base.php';

class AddFloatsTestCase extends TestServiceTestCase {

    public function test_add_floats_null() {
        $this->assertEquals($this->service->add_floats(null, null), 0);
    }

    public function test_add_floats() {
        $this->assertEquals($this->service->add_floats(100, 50), 150);
    }

}
