import re

from datetime import datetime, date, tzinfo, timedelta
from time import mktime

from pyws.errors import MissingFieldValue, WrongFieldValueType


class NotImplemented(NotImplementedError):
    pass


class UnknownType(Exception):

    def __init__(self, type_):
        self.type = type_
        super(UnknownType, self).__init__(type_)

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
    _represents = None

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, type) and issubclass(type_, cls._represents)

    @classmethod
    def get(cls, type_):
        return cls

    @classmethod
    def validate(cls, value, none_value=None):
        if value is not None:
            return cls._validate(value)
        if none_value is None:
            none_value = cls.none_value
        if callable(none_value):
            return none_value()
        return none_value

    @classmethod
    def _validate(cls, value):
        raise NotImplemented('SimpleType._validate')

    @classmethod
    def serialize(cls, value):
        return unicode(value)

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


class Date(Type):

    _represents = date
    format = '%Y-%m-%d'

    @classmethod
    def _parse(cls, value, format=None):
        return datetime.strptime(value, format or cls.format)

    @classmethod
    def _validate(cls, value):
        return cls._parse(value).date()

    @classmethod
    def serialize(cls, value):
        return datetime.strftime(value, cls.format)


class DateTime(Date):

    _represents = datetime
    format = '%Y-%m-%dT%H:%M:%S'
    tz_re = re.compile('((\\+|-)(\d\d):?(\d\d))$')

    @classmethod
    def default_offset(cls):
        return -mktime(datetime(1970, 1, 1).timetuple())

    @classmethod
    def get_offset(cls, value):
        if value[-1] == 'Z':
            return value[:-1], 0
        tz = cls.tz_re.search(value)
        if not tz:
            return value, 0
        return (
            cls.tz_re.sub('', value),
            (tz.group(2) == '+' and 1 or -1) *
                (int(tz.group(3)) * 60 + int(tz.group(4))) * 60
        )

    @classmethod
    def get_tzinfo(cls, offset):
        class TempTzInfo(tzinfo):
            def utcoffset(self, dt):
                return timedelta(seconds=offset)
            def dst(self, dt):
                return timedelta(0)
        return TempTzInfo()

    @classmethod
    def _validate(cls, value):
        value, offset = cls.get_offset(value)
        tz = cls.get_tzinfo(offset)
        try:
            return cls._parse(value).replace(tzinfo=tz)
        except ValueError:
            mo = re.search('\\.\d+', value)
            if not mo:
                raise
            ms = mo.group(0)
            value = value.replace(ms, ms.ljust(7, '0'))
            return cls._parse(value, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=tz)

    @classmethod
    def serialize(cls, value):
        if value.tzinfo:
            delta = value.utcoffset() + value.dst()
        else:
            delta = timedelta(seconds=cls.default_offset())
        value = value.replace(tzinfo=cls.get_tzinfo(0)) - delta
        return super(DateTime, cls).serialize(value) + 'Z'


DICT_NAME_KEY = 0

class Dict(Type):

    fields = []

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, dict)

    @classmethod
    def get(cls, type_):
        try:
            dict_name = type_[DICT_NAME_KEY]
        except KeyError:
            raise BadType('%s is required for Dict type' % repr(DICT_NAME_KEY))
        fields = [
            isinstance(type_, tuple) and (name,) + type_ or (name, type_)
            for name, type_ in type_.iteritems() if name != DICT_NAME_KEY]
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
    element_type = None
    element_none_value = None

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
    #noinspection PyUnresolvedReferences
    ret.add_fields(*fields)
    return ret


def ListOf(element_type, element_none_value=None):
    return type(element_type.__name__ + 'List', (List,), {
        'element_type': element_type,
        'element_none_value': element_none_value})


# The order matters: DateTime should be placed before Date.
# date is a superclass of datetime, thus Date will catch all DateTime fields.
types = (String, Integer, Float, DateTime, Date, Dict, List)


def TypeFactory(type_):
    if isinstance(type_, type) and issubclass(type_, Type):
        return type_
    for x in types:
        if x.represents(type_):
            return x.get(type_)
    raise UnknownType(type_)
