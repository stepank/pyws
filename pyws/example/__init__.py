from pyws.functions import NativeFunctionAdapter
from pyws.functions.args import String, Integer, Float, DictOf, Field, ListOf

def simple(p):
    return p + ' world'

def simple_integer(p):
    return p * 2

def add_integer(p, q):
    return p + q

def add_dict(p, q):
    return {'a': p['a'] + q['a'], 'b': p['b'] + q['b']}

def add_list(p, q):
    s, b = len(p) < len(q) and p, q or q, p
    s.extend([0] * (len(b) - len(s)))
    return list(s[i] + b[i] for i in xrange(len(s)))

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

ABDict = DictOf('ABDict',
    Field('a', Integer),
    Field('b', Integer),
)

add_dict_adapter = NativeFunctionAdapter(
    add_dict,
    return_type=ABDict,
    args=(
        ('p', ABDict),
        ('q', ABDict),
    ),
)

ListOfInteger = ListOf(Integer)

add_list_adapter = NativeFunctionAdapter(
    add_list,
    return_type=ListOfInteger,
    args=(
        ('p', ListOfInteger),
        ('q', ListOfInteger),
    ),
)

