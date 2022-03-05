#!/usr/bin/env python3

""" this is the FileStorage class definition
module
"""

import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Class that serializes instances to a JSON
    file and deserializes JSON files to instances"""

    def __init__(self):
        """ initialization of FileStorage"""
        self.__file_path = "file.json"
        self.__objects = {}  # emptydict

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        # First, get the object's class name followed bi "." and
        # the id of the object.
        # ex: to store a BaseModel object with id=12121212,
        #  the key will be BaseModel.12121212)

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        # Finally, it stores the object "obj" in self.__objects, at
        # key previously generated.

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)"""
        #  For some reason this returns:
        # TypeError: Object of type BaseModel is not JSON serializable
        # print(self.__objects)
        # for key in self.__objects:
        #    if key == "created_at" or key == "updated_at":
        #        self.__objects[key] = self.__objects[key].isoformat()
        #        print(f"{key} : {self.__objects[key]}")
        # json.dumps(self.__objects, indent=4, sort_keys=True, default=str)
        with open(self.__file_path, "w", encoding='utf-8') as f:
            # for obj in self.__objects.values():
            #     key = obj.__class__.__name__ +"."+ obj.id
            #     new_dict[key] = obj.to_dict()
            #     json.dump(new_dict, f)
            #     f.write(',')
            # for each item in self.__objects, made of a pair of key
            # and value, turn the value to dict, and then dump it to
            # json file
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()}, f)
            # f.write(json.dumps(self.__objects))
            # The issue is that json.dump cant serialize a datetime object
            # that easily. It needs a way to represent it as a string.
            # this solution almost works, but there is an extra pair of
            # quotes at the end of the cat file.json ; echo ""

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn
        t exist, no exception should be raisedi)"""

        classes = {'BaseModel': BaseModel, "User": User,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place, "Review": Review}

        try:
            with open(self.__file_path, 'r') as f:
                obj = json.load(f)
                for keys, values in obj.items():
                    tmp = keys.split('.')
                    new = classes[tmp[0]](**values)
                    self.new(new)
        except FileNotFoundError:  # pycodestyle said not to use
            # except bare
            pass  # If the file doesnt exist, no exception should be raised)
