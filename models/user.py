#!/usr/bin/python3
""" User for console """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ user instantiation"""
        super().__init__(*args, **kwargs)