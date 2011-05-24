from pyws.errors import MissingFieldValue, WrongFieldValueType


class NotImplemented(NotImplementedError):
    pass


class Field(object):

    def __init__(self, name, type, none_value=None):
        self.name = name
        self.type = type
        self.none_value = none_value

    def get_value(self, data):
        try:
            return data[self.name]
        except KeyError:
            raise MissingFieldValue(self.name)

    def validate(self, value):
        try:
            return self.type.validate(value, self.none_value)
        except ValueError:
            raise WrongFieldValueType(self.name)


class Type(object):

    none_value = None

    @classmethod
    def validate(cls, value, none_value=None):
        if value is None:
            if none_value is not None:
                return none_value
            else:
                return cls.none_value
        return cls._validate(value)

    @classmethod
    def _validate(cls, value):
        raise NotImplemented('SimpleType._validate')


class String(Type):

    none_value = ''

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, basestring):
            raise ValueError(value)
        return unicode(value)


class Integer(Type):

    @classmethod
    def _validate(cls, value):
        return int(value)


class Float(Type):

    @classmethod
    def _validate(cls, value):
        return float(value)


class Dict(Type):

    @classmethod
    def add_fields(cls, *fields):
        fields_ = []
        for field in fields:
            if isinstance(field, Field):
                fields_.append(field)
            else:
                fields_.append(Field(*field))
        cls.fields += fields_

    @classmethod
    def _validate(cls, value):
        return dict(
            (field.name, field.validate(field.get_value(value)))
                for field in cls.fields)


class List(Type):

    none_value = []

    @classmethod
    def _validate(cls, value):
        return [cls.element_type.validate(val, cls.element_none_value)
            for val in value]


def DictOf(name, *fields):
    ret = type(name, (Dict, ), {'fields': []})
    ret.add_fields(*fields)
    return ret

def ListOf(element_type, element_none_value=None):
    return type(element_type.__name__ + 'List', (List, ), {
        'element_type': element_type,
        'element_none_value': element_none_value})
