import re

from datetime import datetime, date, tzinfo, timedelta
from time import mktime

from pyws.functions.args.types.base import Type

__all__ = ('String', 'Integer', 'Float', 'Date', 'DateTime', )


class String(Type):
    """
    Represents strings, simplified form is ``str``, default ``none_value`` is
    ``''``.
    """

    none_value = ''

    _represents = basestring

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, basestring):
            raise ValueError(value)
        return unicode(value)


class Integer(Type):
    """
    Represents integer numbers, simplified form is ``int``, default
    ``none_value`` is ``None``.
    """

    _represents = int

    @classmethod
    def _validate(cls, value):
        return int(value)


class Float(Type):
    """
    Represents floating point numbers, simplified form is ``float``, default
    ``none_value`` is ``None``.
    """

    _represents = float

    @classmethod
    def _validate(cls, value):
        return float(value)


class Date(Type):
    """
    Represents date values, simplified form is ``date``, default
    ``none_value`` is ``None``.
    """

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


tz_re = re.compile('((\\+|-)(\d\d):?(\d\d))$')

class DateTime(Date):
    """
    Represents datetime values, simplified form is ``datetime``, default
    ``none_value`` is ``None``.
    """

    _represents = datetime
    format = '%Y-%m-%dT%H:%M:%S'

    @classmethod
    def default_offset(cls):
        return -mktime(datetime(1970, 1, 1).timetuple())

    @classmethod
    def get_offset(cls, value):
        if value[-1] == 'Z':
            return value[:-1], 0
        tz = tz_re.search(value)
        if not tz:
            return value, 0
        return (
            tz_re.sub('', value),
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
