#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

try:
    #noinspection PyUnresolvedReferences
    import lxml
except ImportError:
    print 'error: lxml is required'
    exit()

setup(
    name='pyws',
    version='dev',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Python SOAP server providing WSDL',
    long_description='Python SOAP server providing WSDL',
    keywords=['soap', 'wsdl', 'server'],
    author='Stepan N. Kornyakov',
    author_email='stepankk@gmail.com',
    url='https://github.com/stepank/pyws',
    license='MIT',
    platforms=['Any'],
)
