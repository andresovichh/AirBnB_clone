#!/usr/bin/python3
""" Console for AirBnb Proyect """
from datetime import datetime
from uuid import uuid4
import json


class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute with the current datetime """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance 
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
