#!/usr/bin/python3
""" Test State File """
from models.user import User
import unittest


class Test_User(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(User.__doc__) > 0)

        def test_documentation(self):
            """documentation for the init method"""

            self.assertTrue(len(User.__init.__doc__) > 0)
