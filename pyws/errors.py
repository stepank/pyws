class Error(Exception):
    pass

class ProtocolError(Error):
    pass

class ProtocolNotFound(ProtocolError):
    def __str__(self):
        return 'A protocol cannot be found: %s' % self.args[0]

class BadProtocol(ProtocolError):
    def __str__(self):
        return 'Bad protocol: %s' % self.args[0]

class FunctionError(Error):
    pass

class FunctionNotFound(FunctionError):
    def __str__(self):
        return 'A function cannot be found: %s' % self.args[0]

class BadFunction(FunctionError):
    def __str__(self):
        return 'Bad function: %s' % self.args[0]
