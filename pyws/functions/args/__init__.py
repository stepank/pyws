class Field(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def validate(self, value):
        return self.type.validate(value)


class SimpleType(object):

    @classmethod
    def validate(cls, value):
        raise NotImplemented('SimpleType.validate')


class String(SimpleType):

    @classmethod
    def validate(cls, value):
        if isinstance(value, list):
            value = value[0]
        return str(value)


class Integer(SimpleType):

    @classmethod
    def validate(cls, value):
        return int(value)


class Float(SimpleType):

    @classmethod
    def validate(cls, value):
        return float(value)


class ListBase(SimpleType):

    @classmethod
    def validate(cls, value):
        return [cls.element_type.validate(val) for val in value]


class RecordBase(SimpleType):

    @classmethod
    def validate(cls, value):
        return dict((field.name, field.validate(value[field.name]))
            for field in cls.fields)


class ComplexType(type):

    def __new__(cls, fields=None):
        return type('ComplexType', (cls.base, ), fields or {})


class List(type):

    def __new__(cls, element_type):
        return type(element_type.__name__ + 'List',
            (ListBase, ), {'element_type': element_type})


class Record(type):

    def __new__(cls, name, *fields):
        return type(name + 'Record', (RecordBase, ), {'fields': fields})
