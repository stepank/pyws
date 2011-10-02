<?
require_once 'base.php';

class AddIntegersTestCase extends TestServiceTestCase {

    public function test_null() {
        $this->assertEquals($this->service->add_integers(null, null), 0);
    }

    public function test() {
        $this->assertEquals($this->service->add_integers(100, 50), 150);
    }

}
