#!/usr/bin/env python3

""" tests for REview"""

from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """ Test State Class """

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Review.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Review.__init__.__doc__) > 0)
