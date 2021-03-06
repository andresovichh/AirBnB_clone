#!/usr/bin/python3
"""
Console for AirBnb Proyect

PLEASE CHECK THAT: storage is instanciated at
__init__.py file located in models

>>> o = BaseModel()
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Instantiation of BaseModel """

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
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(str(self.__class__.__name__),
                                     str(self.id), str(self.__dict__))

    def save(self):
        """ updates the public instance attribute with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
