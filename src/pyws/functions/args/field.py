from pyws.errors import MissingFieldValue, WrongFieldValueType
from pyws.functions.args.types import TypeFactory

__all__ = ('Field', 'FieldFactory', )


class Field(object):
    """
    A field combines a name, a type and a value that represents an empty value.
    """

    def __init__(self, name, type_, none_value=None):
        """
        ``name`` is the name of a field. ``type_`` is its type and
        ``none_value`` represents an empty value, callables are accepted as
        well. ``type_`` can be specified in both standard and simplified form,
        more on that read in chapter :ref:`type_specification`. ``none_value``
        is used to replace ``None``, if field's ``none_value`` is ``None`` then
        that of its type is used.
        """
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
