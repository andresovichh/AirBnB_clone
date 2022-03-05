#!/usr/bin/python3

""" Creating a unique FileStorage instance for our
application

1) Importing file_storage.py

2) Creating variable storage, an instance of FileStorage

3) calling reload() method on storage

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
