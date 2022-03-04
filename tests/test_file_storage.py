#!/usr/bin/python3
""" TEst FileStorage """
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """ Test FileStorage """

    def test_new(self):
        """ Test if key is correct """
        self.assertEqual(FileStorage.obj, "BaseModel.12121212")
