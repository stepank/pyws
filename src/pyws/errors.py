ET_CLIENT = 1
ET_SERVER = 2


class ConfigurationError(Exception):
    pass


class ServerAlreadyRegistered(ConfigurationError):
    def __str__(self):
        return 'Server %s has already been registered' % self.args[0]


class SettingNotDefined(ConfigurationError):
    def __str__(self):
        return 'Setting %s is not defined' % self.args[0]


class NoProtocolsRegistered(ConfigurationError):
    def __str__(self):
        return 'Server has no protocols'


class Error(Exception):
    error_type = ET_SERVER


class ClientErrorTypeMixin(Exception):
    error_type = ET_CLIENT


class ProtocolError(Error):
    pass


class ProtocolNotFound(ProtocolError):

    def __str__(self):
        return 'A protocol cannot be found: %s' % self.args[0]


class BadProtocol(ProtocolError):

    def __str__(self):
        return 'Bad protocol: %s' % self.args[0]


class BadRequest(ClientErrorTypeMixin, ProtocolError):

    def __str__(self):
        if not self.args:
            return 'Bad request'
        return 'Bad request: %s' % self.args[0]


class AccessDenied(ClientErrorTypeMixin, ProtocolError):

    def __str__(self):
        if not self.args or not self.args[0]:
            return 'Access denied'
        return 'Access denied for user %s' % self.args[0]


class FunctionError(Error):
    pass


class FunctionNotFound(ClientErrorTypeMixin, FunctionError):

    def __str__(self):
        return 'A function cannot be found: %s' % self.args[0]


class BadFunction(FunctionError):

    def __str__(self):
        return 'Bad function: %s' % self.args[0]


class FieldError(ClientErrorTypeMixin, Error):
    pass


class MissingFieldValue(FieldError):

    def __str__(self):
        return 'The value of \'%s\' field is missing.' % self.args[0]


class WrongFieldValueType(FieldError):

    def __str__(self):
        return 'The value of \'%s\' field is of wrong type.' % self.args[0]
