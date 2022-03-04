#!/usr/bin/env python3

""" unittest for BaseModel Class"""

import json
import unittest
import pep8
from models.base_model import BaseModel
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

class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        # """Test that we conform to PEP8."""
        # pep8style = pep8.StyleGuide(quiet=True)
        # result = pep8style.check_files(['base.py'])
        # print(result)
        # self.assertEqual(result.total_errors, 0,
        #                  "Found code style errors (and warnings).")
        # https://pep8.readthedocs.io/en/release-1.7.x/intro.html
        fchecker = pep8.Checker('models/base_model.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)

if __name__ == "__main__":
    unittest.main()