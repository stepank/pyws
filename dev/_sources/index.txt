Welcome to pyws's documentation!
================================

Good day!

I hope this document will help you working with pyws. If you have any comments,
questions, suggestions, problems, or anything else to say, feel free to contact
me via email stepankk@gmail.com. pyws code is hosted on GitHub at
https://github.com/stepank/pyws.


.. _requirements:

Requirements
============

pyws itself depends only on python standard library and lxml. I've tested pyws
on python 2.6 and python 2.7.

pyws is written the way that it might be integrated with any web server and
python framework; it is achieved by using different adapters:

* :ref:`django_adapter` depends on Django, I use 1.3;
* :ref:`twisted_web_adapter` depends on Twisted, I use 11.0.0;
* :ref:`wsgi_adapter` depends on wsgiref, I use 0.1.2.


.. _installation:


Installation
============

The easiest way to install pyws is to run::

    easy_install pyws

Or you might download source distribution archive from PyPI (available at
http://pypi.python.org/pypi/pyws) or clone GIT repo. In these cases you ought
to change current directory to the root of pyws's distribution package and
run::

    python setup.py install


Topics
========

.. toctree::
   :maxdepth: 3

   introduction
   complete_reference
   integration_tests
