#!/usr/bin/env python3

import json
from models.base_model import BaseModel

class Filestorage(BaseModel):
    """ Class that serializes instances to a JSON
    file and deserializes JSON files to instances"""
    
    def __init__(self):
        Filestorage.__file_path = "file.json"
        Filestorage.__objects = {} # emptydict

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects.__dict__

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        algo con setattr
    
    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)"""
        from python to json
    
    def reload(self):
        """ deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists 
        otherwise, do nothing. If the file doesn
        t exist, no exception should be raised)"""



