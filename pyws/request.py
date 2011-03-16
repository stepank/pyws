class Request(object):

    def __init__(self, tail, text, GET, POST, COOKIES):
        self.tail = tail.strip('/')
        self.text = text
        self.GET = GET
        self.POST = POST
        self.COOKIES = COOKIES
