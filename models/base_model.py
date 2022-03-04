#!/usr/bin/python3
""" Console for AirBnb Proyect

PLEASE CHECK THAT: storage is instanciated at
__init__.py file located in models

 """

import json
from uuid import uuid4
import models
from datetime import datetime

class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializing BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():

                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')

                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)
        # not sure if this is what 5 is
        # asking for.

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    # def defaultconverter(self):
    #    if isinstance(self.updated_at, datetime.datetime):
    #        return self.updated_at.__str__()
    #    if isinstance(self.created_at, datetime.datetime):
    #        return self.created_at.__str__()

    def save(self):
        """ updates the public instance attribute with the current datetime """
        self.updated_at = datetime.today()
        models.storage.save()
        # second line should be calling the save method on
        # storage, which was imported from models

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
