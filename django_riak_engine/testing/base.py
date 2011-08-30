from django.test.utils import setup_test_environment
from django.utils import unittest


class BaseTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        super(BaseTestCase, self).setUp()
        setup_test_environment()
