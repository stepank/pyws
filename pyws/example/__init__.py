from datetime import date, datetime

from pyws.functions import NativeFunctionAdapter
from pyws.functions.args import DictOf

def add_simple(a, b):
    return a + b

def next_month(d):
    if not d:
        return None
    month = d.month + 1
    year = d.year
    if month > 12:
        month = (d.month - 1) % 12 + 1
        year += 1
    return d.replace(year=year, month=month)

def add_dicts(p, q):
    return {
        'a': p['a'] + q['a'],
        'b': p['b'] + q['b'],
    }

def add_string_lists(p, q):
    if len(p) < len(q):
        p.extend([''] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([''] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))

def add_integer_lists(p, q):
    if len(p) < len(q):
        p.extend([0] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([0] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))

def sum_tree(p):
    return p and (p['value'] +
        (p['left'] and sum_tree(p['left']) or 0) +
        (p['right'] and sum_tree(p['right']) or 0)) or 0

def get_tree(p):
    if not p:
        return None
    if p == 1:
        return {'value': 1}
    if p == 2:
        return {'value': 2, 'left': None, 'right': None}
    return {
        'value': 3,
        'left': {'value': 4, 'left': None, 'right': None},
        'right': {'value': 5, 'left': None, 'right': None},
    }

needs_auth_adapter = NativeFunctionAdapter(
    add_simple, name='needs_auth', needs_auth=True)

class HelloError(Exception):
    def __init__(self):
        super(HelloError, self).__init__('hello error')

def raises_exception():
    raise HelloError

add_integers_adapter = NativeFunctionAdapter(
    add_simple,
    name='add_integers',
    return_type=int,
    args=(
        (int, 0),
        (int, 0),
    ),
)

add_floats_adapter = NativeFunctionAdapter(
    add_simple,
    name='add_floats',
    return_type=float,
    args=(
        (float, 0),
        (float, 0),
    ),
)

next_month_adapter = NativeFunctionAdapter(
    next_month,
    name='next_month',
    return_type=date,
    args=(date, ),
)

next_month_dt_adapter = NativeFunctionAdapter(
    next_month,
    name='next_month_dt',
    return_type=datetime,
    args=(datetime, )
)

ABStringDict = {
    '__name__': 'ABStringDict',
    'a': str,
    'b': str,
}

add_string_dicts_adapter = NativeFunctionAdapter(
    add_dicts,
    name='add_string_dicts',
    return_type=ABStringDict,
    args=(
        (ABStringDict, {'a': '', 'b': ''}),
        (ABStringDict, {'a': '', 'b': ''}),
    ),
)

ABIntegerDict = {
    '__name__': 'ABIntegerDict',
    'a': (int, 0),
    'b': (int, 0),
}

add_integer_dicts_adapter = NativeFunctionAdapter(
    add_dicts,
    name='add_integer_dicts',
    return_type=ABIntegerDict,
    args=(
        (ABIntegerDict, {'a': 0, 'b': 0}),
        (ABIntegerDict, {'a': 0, 'b': 0}),
    ),
)

StringList = [str]

add_string_lists_adapter = NativeFunctionAdapter(
    add_string_lists,
    name='add_string_lists',
    return_type=StringList,
    args=(StringList, StringList),
)

IntegerList = [int, 0]

add_integer_lists_adapter = NativeFunctionAdapter(
    add_integer_lists,
    name='add_integer_lists',
    return_type=IntegerList,
    args=(IntegerList, IntegerList),
)

Tree = DictOf('Tree',
    ('value', int, 0),
)
Tree.add_fields(
    ('left', Tree),
    ('right', Tree),
)

sum_tree_adapter = NativeFunctionAdapter(
    sum_tree,
    return_type=int,
    args=(Tree,),
)

get_tree_adapter = NativeFunctionAdapter(
    get_tree,
    return_type=Tree,
    args=(int,),
)
