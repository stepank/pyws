<?
ini_set('display_errors', true);
error_reporting(E_ALL);

require_once 'TestService.php';

class TestServiceTestCase extends PHPUnit_Framework_TestCase {

    protected function setUp() {
        $this->service = new TestService('test.wsdl',
            array('cache_wsdl' => WSDL_CACHE_NONE, 'trace' => true));
    }

    public function test_simple() {
        $this->assertEquals($this->service->simple('hello'), 'hello world');
    }

    public function test_simple_integer() {
        $this->assertEquals($this->service->simple_integer(100), 200);
    }

    public function test_simple_float() {
        $this->assertEquals($this->service->simple_float(100), 200);
    }

    public function test_add_integer() {
        $this->assertEquals($this->service->add_integer(100, 50), 150);
    }

    public function test_add_float() {
        $this->assertEquals($this->service->add_float(100, 50), 150);
    }

}
