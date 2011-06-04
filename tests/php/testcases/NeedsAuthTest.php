<?
require_once 'base.php';

class NeedsAuthTestCase extends TestServiceTestCase {

    protected function setUp() {
        parent::setUp();
        $headers = new HeadersDict();
        $headers->username = 'user';
        $headers->password = 'pass';
        $header = new SoapHeader(
            'http://example.com/', 'headers', $headers);
        $this->service->__setSoapHeaders($header);
    }

    public function test_needs_auth() {
        $this->assertEquals(
            $this->service->needs_auth('hello', ' world'), 'hello world');
    }
}
