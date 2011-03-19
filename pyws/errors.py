ET_CLIENT = 0
ET_SERVER = 1

class Error(Exception):
    error_type = ET_SERVER

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
    error_type = ET_CLIENT
    def __str__(self):
        return 'A function cannot be found: %s' % self.args[0]

class BadFunction(FunctionError):
    def __str__(self):
        return 'Bad function: %s' % self.args[0]
