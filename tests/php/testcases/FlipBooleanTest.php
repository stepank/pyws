<?
require_once 'base.php';

class FlipBooleanTestCase extends TestServiceTestCase {

    public function test_null() {
        $this->assertEquals($this->service->flip_boolean(null), true);
    }

    public function test_numeric() {
        $this->assertEquals($this->service->flip_boolean(0), true);
    }

    public function test() {
        $this->assertEquals($this->service->flip_boolean(true), false);
        $this->assertEquals($this->service->flip_boolean(false), true);
    }
}
