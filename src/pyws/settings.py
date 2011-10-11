from itertools import chain

from pyws.errors import SettingNotDefined

def check_exists(func):
    def decorated(self, instance, *args, **kwargs):
        if self.attr_name not in instance.state:
            raise SettingNotDefined(self.attr_name)
        return func(self, instance, *args, **kwargs)
    return decorated


class Slot(object):

    attr_name = None

    #noinspection PyUnusedLocal
    @check_exists
    def __get__(self, instance, owner):
        return instance.state[self.attr_name]

    def __set__(self, instance, value):
        instance.state[self.attr_name] = value

    @check_exists
    def __delete__(self, instance):
        del instance.state[self.attr_name]


class DictSlot(Slot):

    def __set__(self, instance, value):
        instance.state.setdefault(self.attr_name, {})
        instance.state.get(self.attr_name).update(value)


class ListSlot(Slot):

    def __set__(self, instance, value):
        instance.state[self.attr_name] = \
            list(chain(instance.state.get(self.attr_name, ()), value))


class Settings(object):

    state = None

    NAME = Slot()
    DEBUG = Slot()
    DEFAULT = Slot()
    PROTOCOLS = ListSlot()
    FUNCTION_MANAGERS = ListSlot()
    CREATE_CONTEXT = Slot()
    DESTROY_CONTEXT = Slot()

    def __init__(self, **state):
        self.state = state
        self.init_slots()

    def init_slots(self, cls=None):
        if not cls:
            cls = type(self)
        for base in cls.__bases__:
            self.init_slots(base)
        for key, value in cls.__dict__.iteritems():
            if isinstance(value, Slot):
                value.attr_name = key

    def update(self, source):
        if isinstance(source, Settings):
            source = source.state
        elif hasattr(source, '__dict__'):
            source = dict(
                pair for pair in source.__dict__.iteritems()
                    if not pair[0].startswith('__'))
        for key, value in source.iteritems():
            setattr(self, key, value)
