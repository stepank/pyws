from pyws.functions import SimpleFunctionAdapter
from pyws.functions.args import String, Integer, Float

def simple(p):
    return p + ' world'

def simple_integer(p):
    return p * 2

simple_integer_adapter = SimpleFunctionAdapter(
    simple_integer,
    return_type=Integer,
    args=(('p', Integer), ),
)

simple_float_adapter = SimpleFunctionAdapter(
    simple_integer,
    name='simple_float',
    return_type=Float,
    args=(('p', Float), ),
)
