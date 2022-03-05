#!/usr/bin/env python3

""" unittest for the console"""

import json
import unittest
from console import HBNBCommand
from datetime import datetime


class TestBase(unittest.TestCase):
    """ initial test class"""
    # 1. Test if documentation present
    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 0)

    def test_documentations1(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.close.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 0)

    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 0)
    # 2. Test if __str__ method prints as expected
# class TestBaseModel(unittest.TestCase):
#     """ Tests for the BaseModel Class"""
#     def test__str__(self):
#         """ test if __str__ method prints as expected"""
#         str_class = BaseModel()
#         string = "[BaseModel] ({}) {}".f
# ormat(str_class.id, str_class.__dict__)
#         self.assertEqual(str(str_class), string)
#     def test_save(self):
#         """ Check if save correctly updates attribute
#         to second and minute"""
#         created = BaseModel().created_at
#         self.assertEqual(created.second, datetime.today().second)
#         self.assertEqual(created.minute, datetime.today().minute)
#     def test_class_name(self):
#         """ check if model class name is ok"""
#         name = BaseModel()
#         self.assertEqual(type(name).__name__, "BaseModel")
#     def test_id_print(self):
#         """ chek if correct len id"""
#         my_model = BaseModel()
#         name = "My_First_Model"
#         my_model.my_number = 89
#         self.assertEqual(len(my_model.id), 36)
    # def test_nonexistant_class(self):
    #     """ check for non existing class"""
    #    my_model = something()
    #    self
