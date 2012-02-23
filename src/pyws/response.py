class Response(object):
    """
    Response objects are created by protocols and contain response information,
    adapters have to transform it into the form suitable for the application
    which pyws is integrated with.
    """

    #: Success response status
    STATUS_SUCCESS = 0
    #: Error response status
    STATUS_ERROR = 1

    #: Response text
    text = None
    #: Response content type
    content_type = None
    #: Response status
    status = None

    def __init__(self, text, content_type='text/plain', status=STATUS_SUCCESS):
        self.text = text
        self.content_type = content_type
        self.status = status

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
