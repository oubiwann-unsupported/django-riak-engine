from django_riak_engine.testing import base


class DatabaseWrapperTestCase(base.BaseTestCase):

    def test_creation(self):
        """
        Ensure that all the attributes are set.
        """

    def test_connect_no_connection(self):
        """
        When the wrapper is instantiated, it's not connected. Test before and
        after connect is called to see that conect is doing the right thing.
        """

    def test_connect_not_connected(self):
        """
        Ensure that if there is a connection already and that this connection
        object isn't connected to the database, when connect is called, the
        connection *is* made.
        """

    def test_connect_has_connection(self):
        """
        Ensure that when connect is called and a connection already exists, and
        that connection object is_connected, the connection object is simply
        returned and nothing is done to it (e.g., default port and host
        settings aren't applied, and connect isn't called).
        """
