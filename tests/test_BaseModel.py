#!/usr/bin/env python3

""" unittest for BaseModel Class"""

import json
import unittest
from unittest.mock import Base
from models.base_model import BaseModel
import os
from datetime import datetime


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


class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel Class"""
    def test__str__(self):
        """ test if __str__ method prints as expected"""
        str_class = BaseModel()
        string = "[BaseModel] ({}) {}".format(str_class.id, str_class.__dict__)
        self.assertEqual(str(str_class), string)

    def test_save(self):
        """ Check if save correctly updates attribute
        to second and minute"""
        created = BaseModel().created_at
        self.assertEqual(created.second, datetime.today().second)
        self.assertEqual(created.minute, datetime.today().minute)

    def test_class_name(self):
        """ check if model class name is ok"""
        name = BaseModel()
        self.assertEqual(type(name).__name__, "BaseModel")

    def test_id_print(self):
        """ chek if correct len id"""
        my_model = BaseModel()
        name = "My_First_Model"
        my_model.my_number = 89
        self.assertEqual(len(my_model.id), 36)

    # def test_nonexistant_class(self):
    #     """ check for non existing class"""
    #    my_model = something()
    #    self
