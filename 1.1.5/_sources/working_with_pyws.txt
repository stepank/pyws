Workflow
========

Actually, pyws is not a server, it's a library allowing developers to easily
integrate SOAP based web services into a web project. The basic workflow looks
like this:

#. create and configure a pyws server,
#. register some functions to it,
#. attach the server to your project using an adapter,
#. enjoy.

A more sophisticated scenario, however, might also include:

* using several protocols as well as creating them,
* dealing with context data, i.e. authentication,
* implementing advanced function access via function managers,
* creating different adapters,
* whatever you want else as long as you can implement it yourself :).


How it works
============

The entry point to pyws is an :ref:`adapter <adapters>`. It can be anything you
want and its role is to tie pyws and your project together. An adapter must
create and feed a :ref:`request <request>` object to a :ref:`server <server>`,
after which the latter performs several actions.

Firstly, the server defines a :doc:`protocol <protocol>`. If there is only one
protocol registered then the server uses it by default, otherwise the server
determines a protocol based on the request data.

Secondly, the server tells the protocol to extract the name of the function to
be called. Then the server asks the protocol to extract context data from the
request and creates a :doc:`context <context>`.

Thirdly, the server tries to find a :ref:`function <function>` by its name,
querying each of its :ref:`function managers <function_manager>`. Then the
server asks the protocol to extract argument values from the request.

Fourthly, the server calls the function with these argument values, complete
argument values validation is performed here too.

Finally, the server creates a :ref:`response <response>` object using the
protocol and returns it to the adapter. That is it.
