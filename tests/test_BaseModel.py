#!/usr/bin/env python3

""" unittest for BaseModel Class"""

import json
import unittest
from models.base_model import BaseModel
import os

class TestBase(unittest.TestCase):
    """ initial test class"""
    # 1. Test if documentation present
    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(BaseModel.__doc__) > 0)
    
    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)

    def test_documentations1(self):
        """check if method has doc"""

        self.assertTrue(len(BaseModel.save.__doc__) > 0)
    
    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    # 2. Test if __str__ method prints as expected

    def test__str__(self):
        """ test if __str__ method prints as expected"""
        