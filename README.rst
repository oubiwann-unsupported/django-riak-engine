Please note: this is a *development* README! None of this works yet. When we're
done, this is what you will do to use this product :-)

Also note: this was taken from the MongoDB how-to blog post by Chris Umbel (see
http://www.chrisumbel.com/article/django_python_mongodb_engine_mongo).

Dependencies
============

 * Python
 * Riak
 * Python drivers for Riak
 * Django nonrel
 * Django toolbox
 * Django Riak engine

Setup
=====

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
==================

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


