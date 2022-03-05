#!/usr/bin/python3
""" Test City File """

import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(City.__doc__) > 0)
