class Request(object):

    def __init__(self, tail, text, GET, POST, COOKIES):
        self.tail = tail.strip('/')
        self.text = text
        self.GET = GET
        self.POST = POST
        self.COOKIES = COOKIES

    def __str__(self):
        return """<pyws.request.Request
    tail: %s
    GET: %s
    POST: %s
    COOKIES: %s
    text:
%s
>""" % (
            self.tail,
            self.GET,
            self.POST,
            self.COOKIES,
            self.text.strip(),
        )

    def __unicode__(self):
        return unicode(self.__str__())
