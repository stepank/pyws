<?
require_once 'base.php';

class NeedsAuthTestCase extends TestServiceTestCase {

    protected function setUp() {
        parent::setUp();
        $headers = new Headers();
        $headers->username = 'user';
        $headers->password = 'pass';
        $this->service->__setSoapHeaders(
            new SoapHeader('http://example.com/', 'headers', $headers));
    }

    public function test_needs_auth() {
        $this->assertEquals(
            $this->service->needs_auth('hello', ' world'), 'hello world');
    }
}
