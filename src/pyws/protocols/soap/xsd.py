from lxml import etree as et

from pyws.functions import args

from utils import *


class UnknownType(Exception):

    def __str__(self):
        return 'Unknown type: %s' % self.args[0]


class Type(object):

    _represents = None

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
        raise NotImplementedError('Type.get_name')

    def get_types(self, types, use_element=False):
        raise NotImplementedError('Type.get_types')


class SimpleType(Type):

    def get_types(self, types, use_element=False):
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


class Date(SimpleType):

    _represents = args.Date

    def get_name(self):
        return 'date', 'http://www.w3.org/2001/XMLSchema'


class DateTime(SimpleType):

    _represents = args.DateTime

    def get_name(self):
        return 'dateTime', 'http://www.w3.org/2001/XMLSchema'


class ComplexType(Type):

    def get_children(self, sequence, types):
        raise NotImplementedError('ComplexType.get_children')

    def get_types(self, types, use_element=False):
        if self.name in types:
            return
        if not use_element:
            complexType = et.Element(
                xsd_name('complexType'), name=self.name[0])
            types[self.name] = complexType
        else:
            element = et.Element(xsd_name('element'), name=self.name[0])
            complexType = et.SubElement(element, xsd_name('complexType'))
            types[self.name] = element
        sequence = et.SubElement(complexType, xsd_name('sequence'))
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
            minOccurs='0', maxOccurs='unbounded')
        type.get_types(types)


# The order matters: DateTime should be placed before Date.
# Date is a superclass of DateTime, thus Date will catch all DateTime fields.
__types__ = (String, Integer, Float, DateTime, Date, Dict, List)

def TypeFactory(type, ns=None, nsmap=None):
    for x in __types__:
        if x.represents(type):
            return x(type, ns, nsmap)
    raise UnknownType(type)
