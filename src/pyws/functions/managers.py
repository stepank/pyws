from pyws.errors import BadFunction, FunctionNotFound,\
    FunctionAlreadyRegistered
from pyws.functions import Function


class FunctionManager(object):

    def get_one(self, context, route, protocol):
        """
        Returns a function by its route if it is accessible in the ``context``
        for the ``protocol``. If it is not accessible or does not exist, raises
        ``pyws.errors.FunctionNotFound``. Read more about context in chaper
        :doc:`context` and about functions in chapter :doc:`function`.
        """
        raise NotImplementedError('FunctionManager.get_one')

    def get_all(self, context, protocol):
        """
        Returns a list of functions accessible in the ``context`` for
        the ``protocol``. Read more about context in chaper :doc:`context` and
        about functiona in chapter :doc:`function`.
        """
        raise NotImplementedError('FunctionManager.get_all')


class FixedFunctionManager(FunctionManager):
    """
    A fixed function manager, it has a fixed set of functions.
    """

    def __init__(self, *functions):
        """
        ``functions`` is a list of functions to be registered.
        """
        self.functions = []
        for function in functions:
            self.add_function(function)

    def build_function(self, function):
        if not isinstance(function, Function):
            raise BadFunction(function)
        return function

    def add_function(self, function):
        """
        Adds the function to the list of registered functions.
        """
        if filter(lambda other: function.route == other.route, self.functions):
            raise FunctionAlreadyRegistered(function.name)
        self.functions.append(self.build_function(function))

    def _get_by_protocol(self, protocol):
        return (f for f in self.functions if f.route.check_protocol(protocol))

    def get_one(self, context, route, protocol):
        """
        Returns a function if it is registered, the context is ignored.
        """
        for function in self._get_by_protocol(protocol):
            match, args = function.route.match(route)
            if match:
                return function, args
        raise FunctionNotFound(route)

    def get_all(self, context, protocol):
        """
        Returns a list of registered functions, the context is ignored.
        """
        return list(self._get_by_protocol(protocol))
