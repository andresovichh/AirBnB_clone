#!/usr/bin/env python3

import json
from models.base_model import BaseModel

class Filestorage:
    """ Class that serializes instances to a JSON
    file and deserializes JSON files to instances"""
    
    def __init__(self):
        Filestorage.__file_path = "file.json"
        Filestorage.__objects = {} # emptydict

    def all(self):
        """ returns the dictionary __objects """
        return self.__dict__

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        # First, get the object's class name followed bi "." and
        # the id of the object. 
        # ex: to store a BaseModel object with id=12121212,
        #  the key will be BaseModel.12121212)

        key = obj.__class__ + "." + obj.id
        self.__objects[key] = obj
        # Finally, it stores the object "obj" in self.__objects, at
        # key previously generated. 

    
    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)"""
        json.dump(self.__objects__, self.__file_path)
        # from python to json
    
    def reload(self):
        """ deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists 
        otherwise, do nothing. If the file doesn
        t exist, no exception should be raised)"""



