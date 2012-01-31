from datetime import date, datetime

from pyws.functions.args import DictOf
from pyws.functions.register import register


# = add simple ================================================================

@register()
@register('add_integers', return_type=int, args=((int, 0), (int, 0)))
@register('add_floats', return_type=float, args=((float, 0), (float, 0)))
def add_simple(a, b):
    return a + b


# = say hello ================================================================

@register('say_hello', needs_context=True)
def say_hello(context=None):
    return 'hello ' + context


# = next month ================================================================

@register(return_type=date, args=(date, ))
@register('next_month_dt', return_type=datetime, args=(datetime, ))
def next_month(d):
    if not d:
        return None
    month = d.month + 1
    year = d.year
    if month > 12:
        month = (d.month - 1) % 12 + 1
        year += 1
    return d.replace(year=year, month=month)


# = add dicts =================================================================

ABStringDict = {0: 'ABStringDict', 'a': str, 'b': str}
ABIntegerDict = {0: 'ABIntegerDict', 'a': (int, 0), 'b': (int, 0)}

ab_string_dict_none = lambda: {'a': '', 'b': ''}
ab_integer_dict_none = lambda: {'a': 0, 'b': 0}

@register(
    'add_string_dicts',
    return_type=ABStringDict,
    args=(
        (ABStringDict, ab_string_dict_none),
        (ABStringDict, ab_string_dict_none),
    ),
)
@register(
    'add_integer_dicts',
    return_type=ABIntegerDict,
    args=(
        (ABIntegerDict, ab_integer_dict_none),
        (ABIntegerDict, ab_integer_dict_none),
    ),
)
def add_dicts(p, q):
    return {
        'a': p['a'] + q['a'],
        'b': p['b'] + q['b'],
    }


# = add lists =================================================================

StringList = [str]

@register(
    'add_string_lists',
    return_type=StringList,
    args=(StringList, StringList),
)
def add_string_lists(p, q):
    if len(p) < len(q):
        p.extend([''] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([''] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))

IntegerList = [int, 0]

@register(
    'add_integer_lists',
    return_type=IntegerList,
    args=(IntegerList, IntegerList),
)
def add_integer_lists(p, q):
    if len(p) < len(q):
        p.extend([0] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([0] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))


# = trees =====================================================================

Tree = DictOf('Tree',
    ('value', int, 0),
)
Tree.add_fields(
    ('left', Tree),
    ('right', Tree),
)

@register(return_type=int, args=(Tree,))
def sum_tree(p):
    return p and (p['value'] +
        (p['left'] and sum_tree(p['left']) or 0) +
        (p['right'] and sum_tree(p['right']) or 0)) or 0

@register(return_type=Tree, args=(int,))
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


# = raises exception ==========================================================

class HelloError(Exception):
    def __init__(self):
        super(HelloError, self).__init__('hello error')

@register()
def raises_exception():
    """
    this function will always fail
    """
    raise HelloError
