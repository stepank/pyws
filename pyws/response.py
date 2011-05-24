class Response(object):

    def __init__(self, text, content_type='text/plain'):
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
