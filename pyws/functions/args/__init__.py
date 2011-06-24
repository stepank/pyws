from pyws.errors import MissingFieldValue, WrongFieldValueType


class NotImplemented(NotImplementedError):
    pass


class UnknownType(Exception):

    def __init__(self, type_):
        self.type = type_

    def __str__(self):
        return 'Unknown type: %s' % str(self.type)


class BadType(Exception):
    pass


class Field(object):

    def __init__(self, name, type_, none_value=None):
        self.name = name
        self.type = TypeFactory(type_)
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


def FieldFactory(field):
    if isinstance(field, Field):
        return field
    return Field(*field)


class Type(object):

    none_value = None

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, type) and issubclass(type_, cls._represents)

    @classmethod
    def get(cls, type_):
        return cls

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

    _represents = basestring

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, basestring):
            raise ValueError(value)
        return unicode(value)


class Integer(Type):

    _represents = int

    @classmethod
    def _validate(cls, value):
        return int(value)


class Float(Type):

    _represents = float

    @classmethod
    def _validate(cls, value):
        return float(value)


class Dict(Type):

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, dict)

    @classmethod
    def get(cls, type_):
        try:
            dict_name = type_['__name__']
        except KeyError:
            raise BadType('__name__ is required for Dict type')
        fields = [
            isinstance(type_, tuple) and (name,) + type_ or (name, type_)
            for name, type_ in type_.iteritems() if name != '__name__']
        return DictOf(dict_name, *fields)

    @classmethod
    def add_fields(cls, *fields):
        fields_ = []
        for field in fields:
            fields_.append(FieldFactory(field))
        cls.fields += fields_

    @classmethod
    def _validate(cls, value):
        return dict(
            (field.name, field.validate(field.get_value(value)))
                for field in cls.fields)


class List(Type):

    none_value = []

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, list)

    @classmethod
    def get(cls, type_):
        if len(type_) < 0:
            raise BadType(
                'Element type (first element) is required for List type')
        type_[0] = TypeFactory(type_[0])
        return ListOf(*type_)

    @classmethod
    def _validate(cls, value):
        return [cls.element_type.validate(val, cls.element_none_value)
            for val in value]


def DictOf(name, *fields):
    ret = type(name, (Dict,), {'fields': []})
    ret.add_fields(*fields)
    return ret


def ListOf(element_type, element_none_value=None):
    return type(element_type.__name__ + 'List', (List,), {
        'element_type': element_type,
        'element_none_value': element_none_value})


types = (String, Integer, Float, Dict, List)

def TypeFactory(type_):
    print type_, isinstance(type_, type), isinstance(type_, type) and issubclass(type_, Type)
    if isinstance(type_, type) and issubclass(type_, Type):
        return type_
    for x in types:
        if x.represents(type_):
            return x.get(type_)
    raise UnknownType(type_)
