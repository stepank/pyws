<?
require_once 'base.php';

class AddFloatsTestCase extends TestServiceTestCase {

    public function test_null() {
        $this->assertEquals($this->service->add_floats(null, null), 0);
    }

    public function test() {
        $this->assertEquals($this->service->add_floats(10.5, 5.3), 15.8);
    }

}
