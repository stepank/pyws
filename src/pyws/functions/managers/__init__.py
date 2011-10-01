from pyws.errors import BadFunction, FunctionNotFound
from pyws.functions import Function, NativeFunctionAdapter


class FunctionManager(object):

    def build_function(self, function):
        if isinstance(function, Function):
            return function
        elif callable(function):
            return NativeFunctionAdapter(function)
        raise BadFunction(function)

    def get_one(self, context, name):
        raise NotImplementedError('FunctionManager.get_one')

    def get_all(self, context):
        raise NotImplementedError('FunctionManager.get_all')


class FixedFunctionManager(FunctionManager):

    def __init__(self, *functions):
        self.functions = {}
        for function in functions:
            self.add_function(function)

    def add_function(self, function):
        function = self.build_function(function)
        self.functions[function.name] = function

    def get_one(self, context, name):
        try:
            return self.functions[name]
        except KeyError:
            raise FunctionNotFound(name)

    def get_all(self, context):
        return self.functions.values()
