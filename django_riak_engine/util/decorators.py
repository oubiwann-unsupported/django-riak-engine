import functools
import sys

from django.db.utils import DatabaseError

from django_riak_engine.exceptions import RiakDatabaseError


def safe_call(func):
    @functools.wraps(func)
    def _func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RiakDatabaseError, e:
            raise DatabaseError, DatabaseError(*tuple(e)), sys.exc_info()[2]
    return _func
