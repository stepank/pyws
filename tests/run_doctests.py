#!/usr/bin/env python

import doctest
import sys

modules = [
    'pyws.functions.register',
    'pyws.functions.args.types',
    'pyws.functions.args.types.complex',
]

if __name__ == '__main__':
    for module in modules:
        __import__(module)
        doctest.testmod(sys.modules[module])
