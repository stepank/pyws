#!/usr/bin/env python

import doctest
import sys

modules = [
    'pyws.functions',
    'pyws.functions.register',
    'pyws.functions.args.types',
    'pyws.functions.args.types.complex',
    'pyws.protocols.soap',
]

if __name__ == '__main__':
    for module in modules:
        __import__(module)
        doctest.testmod(sys.modules[module])
