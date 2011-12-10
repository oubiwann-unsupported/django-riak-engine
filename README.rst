~~~~~~~~~~~~~~~~~~
django-riak-engine
~~~~~~~~~~~~~~~~~~

.. contents::
   :depth: 3

Please note: this is a *development* README! None of this works yet. When we're
done, this is what you will read to learn about and use this product :-)




============
Introduction
============

About Riak
----------

Riak is a nosql database solution, built with Erlang and designed to duplicate
the functionality of Amazon's Dynamo.

Riak has a pluggable backend for its core shard-partitioned storage, with the
default storage backend being Bitcask. Riak also has
built-in MapReduce with native support for both JavaScript (using the
SpiderMonkey runtime) and Erlang, while supporting a variety of additional
language drivers, including Python.

For a comparison of Riak with other nosql solutions, visit this page:

 * http://wiki.basho.com/Riak-Comparisons.html

For a general nosql comparison, read this blog post:

 * http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis

About django-riak-engine
------------------------

In order to be used in Django-nonrel applications, this project is cenetered
upon creating the necessary database adaptors for Django.

Community
---------

There is a development discussion Google group here for public participation of
anyone interested in coding on the project:

 * http://groups.google.com/group/django-riak-dev




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
your system (add ``sudo`` at beginning if not inside virtualenv)::

    $ easy_install django-riak-engine


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


=====
Usage
=====

Setting up Django
-----------------

Let's get started with a demo app::

  $ django-admin.py startproject riakproj
  $ cd riakproj
  $ django-admin.py startapp riakapp

Configure the app to talk to a specific database in settings.py::

    DATABASES = {
        'default': {
            'ENGINE': 'django_riak_engine.riak',
            'NAME': 'mydatabase',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '8091',
            'SUPPORTS_TRANSACTIONS': False,
        },
    }


Using the Database
------------------

Let's created a model::

    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length = 64)
        content = models.TextField()


And a quick view that exercises it::

    from django.http import HttpResponse
    from models import *

    def testview(request):
      article = Article(title = 'test title',
        content = 'test content')
      article.save()

      return HttpResponse("<h1>Saved!</h1>")

Now let's use the Django Riak API::

    db.riakapp_article.find()

To get a list of all articles::

    articles = Article.objects.all()




====
TODO
====

Infrastructure
--------------

Get the base unit tests set up.

Implementation
--------------

Everything.


Testing
-------

All the implementation.


Documentation
-------------

All the implementation.




=======
Changes
=======

Version 0.1
-----------

* Initial release of django_riak_engine.


