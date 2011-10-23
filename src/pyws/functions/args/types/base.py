__all__ = ('Type', )


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
        raise NotImplementedError('SimpleType._validate')

    @classmethod
    def serialize(cls, value):
        return unicode(value)
