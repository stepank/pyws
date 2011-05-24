<?
ini_set('display_errors', true);
error_reporting(E_ALL);

require_once 'TestService.php';

class TestServiceTestCase extends PHPUnit_Framework_TestCase {

    protected function setUp() {
        $this->service = new TestService('test.wsdl',
            array('cache_wsdl' => WSDL_CACHE_NONE, 'trace' => true));
    }

    public function test_fake() {
        # for PHP unit not to throw warnings
    }
}
