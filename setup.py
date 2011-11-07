#!/usr/bin/env python

import sys, os
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from setuptools import setup
from setuptools import find_packages

import pyws

setup(
    name='pyws',
    version=pyws.VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Python SOAP server providing WSDL',
    long_description='Python SOAP server providing WSDL',
    keywords=['soap', 'wsdl', 'server', 'xml', 'json'],
    author='Stepan N. Kornyakov',
    author_email='stepankk@gmail.com',
    url='https://github.com/stepank/pyws',
    license='MIT',
    platforms=['Any'],
    install_requires=['lxml'],
)
