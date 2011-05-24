from lxml import etree as et

from pyws.functions import args

from utils import * #@UnusedWildImport


class NotImplemented(NotImplementedError):
    pass


class UnknownType(Exception):

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return 'Unknown type: %s' % self.type


class Type(object):

    def __init__(self, type, ns=None, nsmap=None):
        self.type = type
        self.ns = ns
        self.nsmap = nsmap

    @classmethod
    def represents(cls, type):
        return issubclass(type, cls._represents)

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        raise NotImplemented('Type.get_name')

    def get_types(self, types):
        raise NotImplemented('Type.get_types')


class SimpleType(Type):

    def get_types(self, types):
        return {}


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


class ComplexType(Type):

    def get_types(self, types):
        if self.name in types:
            return
        complexType = et.Element(xsd_name('complexType'), name=self.name[0])
        sequence = et.SubElement(complexType, xsd_name('sequence'))
        types[self.name] = complexType
        self.get_children(sequence, types)


class Dict(ComplexType):

    _represents = args.Dict

    def get_name(self):
        return self.type.__name__, self.ns

    def get_children(self, sequence, types):
        for field in self.type.fields:
            type = TypeFactory(field.type, self.ns, self.nsmap)
            element = et.SubElement(sequence,
                xsd_name('element'), name=field.name,
                type=qname(*(type.name + (self.nsmap, ))))
            element.set('nillable', 'true')
            type.get_types(types)


class List(ComplexType):

    _represents = args.List

    def get_name(self):
        return self.type.__name__, self.ns

    def get_children(self, sequence, types):
        type = TypeFactory(self.type.element_type, self.ns, self.nsmap)
        et.SubElement(sequence,
            xsd_name('element'), name='item',
            type=qname(*(type.name + (self.nsmap, ))),
            minOccurs='0', maxOccurs='unbounded', nillable='true')
        type.get_types(types)


types = (String, Integer, Float, Dict, List)

def TypeFactory(type, ns=None, nsmap=None):
    for x in types:
        if x.represents(type):
            return x(type, ns, nsmap)
    raise UnknownType(type)