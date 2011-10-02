<?
ini_set('display_errors', true);
error_reporting(E_ALL);

require_once dirname(dirname(realpath(__FILE__))) . '/TestService.php';

class TestServiceTestCase extends PHPUnit_Framework_TestCase {

    public $service;

    protected function setUp() {
        $this->service = new TestService('test.wsdl',
            array('cache_wsdl' => WSDL_CACHE_NONE, 'trace' => true));
    }

    public function test_fake() {
        # for PHP unit not to throw warnings
    }
}
