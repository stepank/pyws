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
    failed = False
    for module in modules:
        __import__(module)
        if doctest.testmod(sys.modules[module])[0]:
            failed = True

    if failed:
        sys.exit(1)
