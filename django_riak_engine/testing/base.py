import os

from riak.test_server import TestServer

from django.test.utils import setup_test_environment
from django.utils import unittest


class BaseTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        super(BaseTestCase, self).setUp()
        # set up the Django environment
        setup_test_environment()


class RiakTestCase(BaseTestCase):
    """
    RIAK_BIN is an environment variable. This need to be set if you want to use
    this class for testing.
    """
    def setUp(self):
        super(RiakTestCase, self).setUp()
        self.testserver = TestServer(bin_dir=os.environ["RIAK_BIN"])
