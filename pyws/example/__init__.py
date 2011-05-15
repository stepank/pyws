from pyws.functions import NativeFunctionAdapter
from pyws.functions.args import String, Integer, Float

def simple(p):
    return p + ' world'

def simple_integer(p):
    return p * 2

def add_integer(p, q):
    return p + q

simple_integer_adapter = NativeFunctionAdapter(
    simple_integer,
    return_type=Integer,
    args=(('p', Integer), ),
)

simple_float_adapter = NativeFunctionAdapter(
    simple_integer,
    name='simple_float',
    return_type=Float,
    args=(('p', Float), ),
)

add_integer_adapter = NativeFunctionAdapter(
    add_integer,
    return_type=Integer,
    args=(
        ('p', Integer),
        ('q', Integer),
    ),
)

add_float_adapter = NativeFunctionAdapter(
    add_integer,
    name='add_float',
    return_type=Float,
    args=(
        ('p', Float),
        ('q', Float),
    ),
)
