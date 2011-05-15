from pyws.functions import args


class NotImplemented(NotImplementedError):
    pass


class UnknownType(Exception):

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return 'Unknown type: %s' % self.type


class Type(object):

    def __init__(self, type):
        self.type = type

    @classmethod
    def represents(cls, type):
        return issubclass(type, cls._represents)

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        raise NotImplemented('Type.get_name')

    @property
    def schema(self):
        return self.get_name()

    def get_schema(self):
        raise NotImplemented('Type.get_schema')


class SimpleType(Type):

    def get_schema(self):
        return None


class String(SimpleType):

    _represents = args.String

    def get_name(self):
        return 'string', 'http://www.w3.org/2001/XMLSchema'


class Integer(SimpleType):

    _represents = args.Integer

    def get_name(self):
        return 'int', 'http://www.w3.org/2001/XMLSchema'


class Float(SimpleType):

    _represents = args.Float

    def get_name(self):
        return 'float', 'http://www.w3.org/2001/XMLSchema'


class Dict(Type):

    _represents = args.Dict

    def get_name(self):
        raise NotImplemented('Dict.get_name')


class List(Type):

    _represents = args.Dict

    def get_name(self):
        raise NotImplemented('List.get_name')


types = (String, Integer, Float, Dict, List)

def TypeFactory(type):
    for x in types:
        if x.represents(type):
            return x(type)
    raise UnknownType(type)