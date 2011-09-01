from django_riak_engine import connection
from django_riak_engine.testing import base


class RiakConnectionTestCase(base.TestCase):
    """
    """
    def test_creation(self):
        """
        Ensure that everything done in __init__ is as expected.
        """

    def test_connect(self):
        """
        The connection method for this unit test hasn't been implemented yet.
        When it has, the unit test will be updated.
        """

    def test_is_connected(self):
        conn = connection.RiakConnection()
        self.assertEqual(conn.is_connected(), False)
        conn._is_connected = "Something crazy"
        self.assertEqual(conn.is_connected(), "Something crazy")
