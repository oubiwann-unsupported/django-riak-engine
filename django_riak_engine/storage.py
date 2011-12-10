# -*- coding: utf-8 -*-

import uuid
from django.core.files import File
from django.core.files.storage import Storage


def riak_client():
    """
    Later on, replace riak_client() with some context-manager-like or perhaps
    just (in case of automatic pooling+thread-safety) link to riak's connection.
    """
    pass


class LuwakFile(File):
    def __init__(self, name):
        self.name = name
        # self.size = size
        self.file = self
        self.mode = 'w'
        self._cache = None

    @property
    def size(self):
        return len(self.read())

    def open(self, mode=None):
        return self

    def read(self, num_bytes=None):
        with riak_client() as riak:
            self._cache = riak.get_file(self.name)
        return self._cache

    def __iter__(self):
        return self.read()

    def chunks(self, chunk_size=None):
        return self.read()

    def multiple_chunks(chunk_size=None):
        return False

    def write(self, content):
        if self._cache is None:
            self._cache = content
        else:
            self._cache += content

    def close(self):
        with riak_client() as riak:
            riak.store_file(self._cache, self.name)
        self._cache = None


class LuwakFileStorage(Storage):  # filestorage
    def delete(self, name):
        with riak_client() as riak:
            riak.delete_file(name)

    def exists(self, name):
        # XXX: this is bad, but driver doesn't have "is file exists" func
        with riak_client() as riak:
            f = riak.get_file(name)
            if f is not None:
                return True
        return False

    def listdir(self, path):
        raise NotImplementedError(u'listdir on LuwakFileStorage is '
                                  u'not implemented')

    def size(self, name):
        # XXX: this is bad, but driver doesn't have "get file size" func
        with riak_client() as riak:
            f = riak.get_file(name)
            if f is not None:
                return len(f)
        return 0

    def url(self, name):
        raise NotImplementedError('url on LuwakFileStorage is not implemented')

    def _open(self, name, mode='rb'):
        return LuwakFile(name)

    def _save(self, name, content):
        lf = LuwakFile(name)
        lf.write(content)

    def get_available_name(self, name):
        name_func = lambda: uuid.uuid1().hex
        available_name = name_func()
        while self.exists(available_name):
            available_name = name_func()
        return available_name
