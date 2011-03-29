from pyws.errors import BadFunction, FunctionNotFound
from pyws.functions import Function, SimpleFunctionAdapter


class FunctionManager(object):

    def build_function(self, function):
        if isinstance(function, Function):
            return function
        elif callable(function):
            return SimpleFunctionAdapter(function)
        raise BadFunction(function)

    def get_one(self, name):
        raise NotImplementedError('FunctionManager.get_one')

    def get_all(self):
        raise NotImplementedError('FunctionManager.get_all')


class FixedFunctionManager(FunctionManager):

    def __init__(self, *functions):
        self.functions = {}
        for function in functions:
            function = self.build_function(function)
            self.functions[function.name] = function

    def get_one(self, name):
        try:
            return self.functions[name]
        except KeyError:
            raise FunctionNotFound(name)