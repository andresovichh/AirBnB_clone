#!/usr/bin/env python3

import json
from models.base_model import BaseModel

class FileStorage:
    """ Class that serializes instances to a JSON
    file and deserializes JSON files to instances"""
    
    def __init__(self):
        FileStorage.__file_path = "file.json"
        FileStorage.__objects = {} # emptydict

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

        with open(self.__file_path, 'rw', encoding='utf-8') as f: 
            json.dump(self.__objects__, f)
        # from python to json
    
    def reload(self):
        """ deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists 
        otherwise, do nothing. If the file doesn
        t exist, no exception should be raised)"""

        try:
            with open(self.__file_path, 'rw', encoding='utf-8') as f:
               data = json.load(f)
               return data
        except:
            pass # If the file doesnt exist, no exception should be raised)



