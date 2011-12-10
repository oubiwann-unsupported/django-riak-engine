import riak


class RiakConnection(object):
    """
    This object manages all the Riak-specific connection logic, alleviating the
    the problem of maintaining all of this in the django_riak_engine
    DatabaseWrapper class.
    """
    def __init__(self, host="", port="", user="", password=""):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self._is_connected = False

        self.raw_client = None  # riak client should be accessible here

    def connect(self):
        pass

    def is_connected(self):
        return self._is_connected
