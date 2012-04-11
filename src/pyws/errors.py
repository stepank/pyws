from pyws.utils import DefaultStrImplemntationMixin

ET_CLIENT = 1
ET_SERVER = 2


class ConfigurationError(DefaultStrImplemntationMixin, Exception):
    pass


class ServerAlreadyRegistered(ConfigurationError):
    def __unicode__(self):
        return u'Server %s has already been registered' % self.args[0]


class DefaultServerAlreadyRegistered(ConfigurationError):
    def __unicode__(self):
        return u'Default server has already been registered'


class SettingNotDefined(ConfigurationError):
    def __unicode__(self):
        return u'Setting %s is not defined' % self.args[0]


class NoProtocolsRegistered(ConfigurationError):
    def __unicode__(self):
        return u'Server has no protocols'


class BadProtocol(ConfigurationError):
    def __unicode__(self):
        return u'Bad protocol: %s' % self.args[0]


class FunctionAlreadyRegistered(ConfigurationError):
    def __unicode__(self):
        return u'Function %s is already registered' % self.args[0]


class BadFunction(ConfigurationError):
    def __unicode__(self):
        return u'Bad function: %s' % self.args[0]


class Error(DefaultStrImplemntationMixin, Exception):
    error_type = ET_SERVER


class ClientErrorTypeMixin(Exception):
    error_type = ET_CLIENT


class ProtocolError(Error):
    pass


class ProtocolNotFound(ClientErrorTypeMixin, ProtocolError):
    def __unicode__(self):
        return u'Protocol %s cannot be found' % self.args[0]


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
    def __unicode__(self):
        return u'Function %s cannot be found' % self.args[0]


class FieldError(ClientErrorTypeMixin, Error):
    pass


class MissingFieldValue(FieldError):
    def __unicode__(self):
        return u'The value of field \'%s\' is missing.' % self.args[0]


class WrongFieldValueType(FieldError):
    def __unicode__(self):
        return u'The value of field \'%s\' is of wrong type.' % self.args[0]
