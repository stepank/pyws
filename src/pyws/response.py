class Response(object):
    """
    Response objects contain response information, adapters should transform it
    using into the form suitable for the application which pyws integrated into.
    """

    #: Response text
    text = None
    #: Response content type
    content_type = None

    def __init__(self, text, content_type='text/xml'):
        self.text = text
        self.content_type = content_type

    def __str__(self):
        return """<pyws.response.Response
    content_type: %s
    text:
%s
>""" % (
            self.content_type,
            self.text.strip()
        )

    def __unicode__(self):
        return unicode(self.__str__())
