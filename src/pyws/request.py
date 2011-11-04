class Request(object):
    """
    Request objects contain request, this information is provided by adapters
    in the way that pyws could handle it.
    """

    def __init__(self, tail, text, GET, POST, COOKIES):
        """
        ``tail`` is everything left from URL to which pyws server is attached.
        ``text`` is request text, ``GET``, ``POST`` and ``COOKIES`` are dicts
        of the form ``{'param1': ['value1', 'value2'], ...}``. SOAP protocol
        requires only the first two.
        """
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
