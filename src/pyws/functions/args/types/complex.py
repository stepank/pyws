from pyws.functions.args.types.base import Type

__all__ = ('DICT_NAME_KEY', 'Dict', 'List', 'DictOf', 'ListOf')


DICT_NAME_KEY = 0

class BadType(Exception):
    pass


class Dict(Type):
    """
    Represents dicts, simplified form is
    ``{0: 'dict_name', 'field_name': field_type, ...}``, default ``none_value``
    is ``None``. If you want to create your own ``Dict`` type, you have to
    inherit it from this type and specify ``fields`` attribute, which is a list
    of fields in either standard or simplified form. Or you can just use
    ``DictOf`` factory or simplified form. The name is required because it
    will be propagated to WSDL description.
    """

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
        from pyws.functions.args.field import FieldFactory
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
    """
    Represents lists, simplified form is ``[element_type]``, default
    ``none_value`` is ``[]``. If you want to create your own ``List`` type,
    you have to inherit it from this type and specify ``element_type``
    attribute in either standard or simplified form, and
    ``element_none_value``. Or you can just use ``ListOf`` factory or
    simplified form.
    """

    none_value = staticmethod(lambda: [])
    element_type = None
    element_none_value = None

    @classmethod
    def represents(cls, type_):
        return isinstance(type_, list)

    @classmethod
    def get(cls, type_):
        from pyws.functions.args.types import TypeFactory
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
    """
    This function creates a dict type with the specified name and fields.

    >>> from pyws.functions.args import DictOf, Field
    >>> dct = DictOf(
    ...     'HelloWorldDict', Field('hello', str), Field('hello', int))
    >>> issubclass(dct, Dict)
    True
    >>> dct.__name__
    'HelloWorldDict'
    >>> len(dct.fields)
    2
    """
    ret = type(name, (Dict,), {'fields': []})
    #noinspection PyUnresolvedReferences
    ret.add_fields(*fields)
    return ret


def ListOf(element_type, element_none_value=None):
    """
    This function creates a list type with element type ``element_type`` and an
    empty element value ``element_none_value``.

    >>> from pyws.functions.args import Integer, ListOf
    >>> lst = ListOf(int)
    >>> issubclass(lst, List)
    True
    >>> lst.__name__
    'IntegerList'
    >>> lst.element_type == Integer
    True
    """
    from pyws.functions.args.types import TypeFactory
    element_type = TypeFactory(element_type)
    return type(element_type.__name__ + 'List', (List,), {
        'element_type': element_type,
        'element_none_value': element_none_value})
