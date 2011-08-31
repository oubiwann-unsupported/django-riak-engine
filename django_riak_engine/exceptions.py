from django.db.utils import DatabaseError


class RiakError(Exception):
    """
    """


class RiakDatabaseError(RiakError, DatabaseError):
    """
    """
