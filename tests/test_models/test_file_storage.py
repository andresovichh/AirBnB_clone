#!/usr/bin/env python3

""" unittest for BaseModel Class"""

import json
import unittest
import pep8
from models.engine.file_storage import FileStorage
import os
from datetime import datetime


class TestFilestorage(unittest.TestCase):
    """ initial test class"""
    # 1. Test if documentation present
    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.__init__.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.all.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.new.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.save.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(FileStorage.reload.__doc__) > 0)


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        # """Test that we conform to PEP8."""
        # pep8style = pep8.StyleGuide(quiet=True)
        # result = pep8style.check_files(['base.py'])
        # print(result)
        # self.assertEqual(result.total_errors, 0,
        #                  "Found code style errors (and warnings).")
        # https://pep8.readthedocs.io/en
        # /release-1.7.x/intro.html
        fchecker = pep8.Checker('models/engine/file_storage.py',
                                show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)


if __name__ == "__main__":
    unittest.main()
