#!/usr/bin/env python

import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../src/'))

import doctest

modules = [
    'pyws.functions.register',
    'pyws.functions.args.types',
    'pyws.functions.args.types.complex',
]

if __name__ == '__main__':
    for module in modules:
        __import__(module)
        doctest.testmod(sys.modules[module])
