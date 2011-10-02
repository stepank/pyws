<?
require_once 'base.php';

class RaisesExceptionTestCase extends TestServiceTestCase {

    public function test() {
        try {
            $this->service->raises_exception();
        } catch (SoapFault $e) {
            $this->assertEquals($e->getMessage(), 'hello error');
            return;
        }
        $this->assertTrue(false, 'Exception hasn\'t been thrown');
    }
}
