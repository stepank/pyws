<?
require_once 'base.php';

class NeedsAuthTestCase extends TestServiceTestCase {

    public function test_needs_context() {
        $headers = new Headers();
        $headers->username = 'user';
        $headers->password = 'pass';
        $this->service->__setSoapHeaders(
            new SoapHeader('http://example.com/', 'headers', $headers));
        $this->assertEquals(
            $this->service->say_hello(), 'hello user');
    }

    public function test_needs_context_exception() {
        $headers = new Headers();
        $headers->username = 'fake';
        $headers->password = 'pass';
        $this->service->__setSoapHeaders(
            new SoapHeader('http://example.com/', 'headers', $headers));
        try {
            $this->service->say_hello();
        } catch (SoapFault $e) {
            $this->assertEquals(
                $e->getMessage(), 'Access denied for user fake');
            return;
        }
        $this->assertTrue(false, 'Exception hasn\'t been thrown');
    }
}
