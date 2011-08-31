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


