<?
require_once 'base.php';

class AddIntegersTestCase extends TestServiceTestCase {

    public function test_add_integers_null() {
        $this->assertEquals($this->service->add_integers(null, null), 0);
    }

    public function test_add_integers() {
        $this->assertEquals($this->service->add_integers(100, 50), 150);
    }

}
