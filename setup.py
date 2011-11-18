#!/usr/bin/env python

import sys, os
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from setuptools import setup
from setuptools import find_packages

import pyws

short_description = 'Python SOAP server providing WSDL'
long_description = \
    '''
    Pyws is a project, which purpuse is to help developers to expose some
    functions of their systems as public APIs via SOAP with WSDL description.
    The main idea is to let developers completely forget about SOAP itself and
    make creating of APIs fast and painless.
    '''

setup(
    name='pyws',
    version=pyws.VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description=short_description,
    long_description=long_description,
    keywords=['soap', 'wsdl', 'server', 'xml', 'json'],
    author='Stepan N. Kornyakov',
    author_email='stepankk@gmail.com',
    url='https://github.com/stepank/pyws',
    license='MIT',
    platforms=['Any'],
    install_requires=['lxml'],
)
