#!/usr/bin/python3
""" Test State File """
import unittest
from models.user import User


class Test_State(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(User.__doc__) > 0)
