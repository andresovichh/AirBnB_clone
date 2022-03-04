#!/usr/bin/python3
""" User for console """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create User """
    def __init__(self):
        """ initialization of USER"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
