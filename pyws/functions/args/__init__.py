from pyws.errors import MissingFieldValue, WrongFieldValueType


class NotImplemented(NotImplementedError):
    pass


class Field(object):

    empty_values = (None, )

    def __init__(self, name, type, required=True, default=None):
        self.name = name
        self.type = type
        self.required = required
        self.default = default

    def get_value(self, data):
        try:
            return data[self.name]
        except KeyError:
            if self.required:
                raise MissingFieldValue(self.name)
        return self.default

    def validate(self, value):
        if value in self.empty_values:
            if self.required:
                raise MissingFieldValue(self.name)
            return value
        try:
            return self.type.validate(value)
        except ValueError:
            raise WrongFieldValueType(self.name)


class Type(object):

    @classmethod
    def validate(cls, value):
        raise NotImplemented('SimpleType.validate')


class String(Type):

    @classmethod
    def validate(cls, value):
        if not isinstance(value, basestring):
            raise ValueError(value)
        return unicode(value)


class Integer(Type):

    @classmethod
    def validate(cls, value):
        return int(value)


class Float(Type):

    @classmethod
    def validate(cls, value):
        return float(value)


class Dict(Type):

    @classmethod
    def validate(cls, value):
        fields = cls.fields
        if callable(cls.fields):
            fields = fields()
        return dict(
            (field.name, field.validate(field.get_value(value)))
                for field in fields)


class List(Type):

    @classmethod
    def validate(cls, value):
        if not isinstance(value, list):
            value = [value]
        return [cls.element_type.validate(val) for val in value]


def DictOf(name, *fields):
    return type(name, (Dict, ), {'fields': fields})

def ListOf(element_type):
    return type(element_type.__name__ + 'List',
        (List, ), {'element_type': element_type})
