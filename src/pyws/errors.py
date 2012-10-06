from pyws.utils import DefaultStrImplemntationMixin

ET_CLIENT = 1
ET_SERVER = 2


class Error(DefaultStrImplemntationMixin, Exception):

    error_type = ET_SERVER

    def __unicode__(self):
        if self.__doc__:
            return unicode(self.__doc__.strip() % self.args)
        if self.args:
            return self.args[0]
        return 'unknown error'


class ClientErrorTypeMixin(Exception):
    error_type = ET_CLIENT


class ConfigurationError(Error):
    def __unicode__(self):
        return unicode(self.args[0])


class ServerAlreadyRegistered(ConfigurationError):
    """
    Server '%s' has already been registered
    """


class DefaultServerAlreadyRegistered(ConfigurationError):
    """
    Default server has already been registered
    """


class SettingNotDefined(ConfigurationError):
    """
    Setting '%s' is not defined
    """


class NoProtocolsRegistered(ConfigurationError):
    """
    Server has no protocols
    """


class BadProtocol(ConfigurationError):
    """
    Bad protocol: %s
    """


class FunctionAlreadyRegistered(ConfigurationError):
    """
    Function '%s' is already registered
    """


class BadFunction(ConfigurationError):
    """
    Bad function: %s
    """


class ProtocolError(Error):
    pass


class ProtocolNotFound(ClientErrorTypeMixin, ProtocolError):
    """
    Protocol '%s' cannot be found
    """


class BadRequest(ClientErrorTypeMixin, ProtocolError):
    def __unicode__(self):
        if not self.args:
            return u'Bad request'
        return u'Bad request: %s' % self.args[0]


class AccessDenied(ClientErrorTypeMixin, ProtocolError):
    def __unicode__(self):
        if not self.args or not self.args[0]:
            return u'Access denied'
        return u'Access denied for user %s' % self.args[0]


class FunctionError(Error):
    pass


class FunctionNotFound(ClientErrorTypeMixin, FunctionError):
    """
    Function '%s' cannot be found
    """


class FieldError(ClientErrorTypeMixin, Error):
    pass


class MissingFieldValue(FieldError):
    """
    The value of field '%s' is missing.
    """


class WrongFieldValueType(FieldError):
    """
    The value of field '%s' is of wrong type.
    """
