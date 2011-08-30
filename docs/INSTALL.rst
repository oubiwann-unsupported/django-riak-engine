============
Installation
============

Dependencies
------------

django_riak_engine has the following dependencies:

 * Python
 * Riak
 * Python drivers for Riak
 * Django nonrel
 * Django toolbox
 * Django Riak engine


Development
-----------

If you want to assist with developement of django_riak_engine or use the latest
code we're working on, you can install from the sources. Once you have git
installed, just do the following::

    $ git clone git@github.com:oubiwann/django-riak-engine.git
    $ cd django-riak-engine
    $ make install


Easy Install
------------

You can use the setuptools easy_install script to get django_riak_engine on
your system::

    $ sudo easy_install django-riak-engine


Manual Download
---------------

You can manually download the source tarball from the Python Package Index by
visiting the following URL:

    http://pypi.python.org/pypi/django-riak-engine

You'll need to untar and gunzip the source, cd into the source directory, and
then you can do the usual::

    $ sudo python setup.py install


Checking the Source
-------------------

Once installed, you can test the source code by executing this in your local
source tree::

    $ make check

That will run the test suite and report on ther successes and/or failures.
