#!/usr/bin/python3
""" Test State File """
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """ Test State Class """

    def test_name_string(self):
        """ Test not a single character """
        self.assertEqual(type(State().name), str)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(State.__doc__) > 0)
