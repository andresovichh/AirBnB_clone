#!/usr/bin/env python3

""" unittest for BaseModel Class"""

import json
import unittest
from models.engine.file_storage import FileStorage
import os
from datetime import datetime


class TestBase(unittest.TestCase):
    """ initial test class"""
    # 1. Test if documentation present
    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.__doc__) > 0)
