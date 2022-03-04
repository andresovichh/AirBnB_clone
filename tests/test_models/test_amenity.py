#!/usr/bin/python3
""" Test State File """

from models.amenity import Amenity
import unittest






class Test_Amenity(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Amenity.__doc__) > 0)
    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Amenity.__init__.__doc__) > 0)


