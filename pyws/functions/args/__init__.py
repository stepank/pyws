from pyws.errors import MissingFieldValue, WrongFieldValueType


class Field(object):

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
        try:
            return self.type.validate(value)
        except ValueError:
            raise WrongFieldValueType(self.name)


class SimpleType(object):

    @classmethod
    def validate(cls, value):
        raise NotImplementedError('SimpleType.validate')


class String(SimpleType):

    @classmethod
    def validate(cls, value):
        if not isinstance(value, basestring):
            raise ValueError(value)
        return str(value)


class Integer(SimpleType):

    @classmethod
    def validate(cls, value):
        return int(value)


class Float(SimpleType):

    @classmethod
    def validate(cls, value):
        return float(value)


class DictBase(SimpleType):

    @classmethod
    def validate(cls, value):
        return dict((field.name,
            field.validate(field.get_value(value)))
                for field in cls.fields)


class ListBase(SimpleType):

    @classmethod
    def validate(cls, value):
        if not isinstance(value, list):
            value = [value]
        return [cls.element_type.validate(val) for val in value]


class ComplexType(type):

    def __new__(cls, fields=None):
        return type('ComplexType', (cls.base, ), fields or {})


class Dict(type):

    def __new__(cls, name, *fields):
        return type(name + 'Dict', (DictBase, ), {'fields': fields})


class List(type):

    def __new__(cls, element_type):
        return type(element_type.__name__ + 'List',
            (ListBase, ), {'element_type': element_type})
