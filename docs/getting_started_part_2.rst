Getting started, part 2
=======================

In this tutorial we're going to introduce WSDL and send a couple of requests
using a SOAP client. It is based on the
:doc:`previous one <getting_started_part_1>`, so you'd better walk through it,
if you hadn't before.


Introducing WSDL
----------------

Ok, if you are intereseted in SOAP you might have already heard about WSDL and
what it is. If you hadn't then it's the most wonderful thing about SOAP, it is
a language which may be used to provide a formal specification of a SOAP web
service. This specification can be used to generate clients which can easily
interact with a server taking away all the burden of making and sending
requests from your shoulders.

Having our pyws server running on ``localhost:8000`` and bound to ``/api/`` we
can get it's WSDL description at http://localhost:8000/api/wsdl. You may
want to cast a glance on it, but it isn't necessary.

Now, let's create a client and send a few requests. We will use
`suds <https://fedorahosted.org/suds/>`_, it is written in Python and is quite
pretty to use. Open python console and let's write some code there::

    >>> import suds
    >>> client = suds.client.Client('http://localhost:8000/api/wsdl', cache=None)
    >>> client.service.add_simple('hello ', 'world')
    hello world

That's it! Isn't it awesome? No curl, HTTP, POST and so on, we just call a
method and it just works!


Complex types
-------------

Now it's time to play with some comlex types: lists and dicts.

First, we need to add a couple of functions to the server, again edit
``server.py``, add this::

    @register(return_type=[int], args=([int], ))
    def double_list(a):
        return map(lambda x: x * 2, a)

    ABDict = {0: 'ABDict', 'a': int, 'b': int}

    @register(return_type=ABDict, args=(ABDict, ))
    def double_dict(a):
        return dict((k, v * 2) for k, v in a.iteritems())

The code seems to be quite self-explanatory, the only thing is that
``0: 'ABDict'`` gives the dict a name, it's required as pyws can't just invent
it. Now, restart the server and go back to python console::

    >>> import suds
    >>> client = suds.client.Client('http://localhost:8000/api/wsdl', cache=None)
    >>> lst = client.factory.create('ns0:IntegerList')
    >>> lst.item = range(3)
    >>> client.service.double_list(lst)
    (IntegerList){
       item[] =
          0,
          2,
          4,
     }

    >>> dct = client.factory.create('ns0:ABDict')
    >>> dct.a = 1
    >>> dct.b = 2
    >>> client.service.double_dict(dct)
    (ABDict){
       a = 2
       b = 4
     }

Pretty simple, huh?

Now that you've done with this introduction, you may want to go
:doc:`deeper <working_with_pyws>`.
