#!/usr/bin/python3
""" Test City File """
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(City.__doc__) > 0)

   def test_class(self):
       """ Test idi, name """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel)) 
