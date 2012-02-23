.. _adapters:

Adapters
========

Basically, an adapter does the following things:

#. accepts some context of your application and a pyws server object,
#. builds a pyws request object out of the context,
#. feeds the request to the server and gets a response
   (``pyws.server.Server.process_request`` method),
#. transforms the response into something that matters in the context of your
   application.


.. _django_adapter:

Django adapter
--------------

Django adapter is a simple function:

.. autofunction:: pyws.adapters._django.serve


.. _twisted_web_adapter:

Twisted Web adapter
-------------------

Twisted Web adapter is a simple function:

.. autofunction:: pyws.adapters._twisted.serve


.. _wsgi_adapter:

WSGI adapter
------------

WSGI adapter adapter is an application, it can be created by this function:

.. autofunction:: pyws.adapters._wsgi.create_application
