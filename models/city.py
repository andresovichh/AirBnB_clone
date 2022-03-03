#!/usr/bin/env python3
"""
A City definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ a class definition of City"""
    def __init__(self):
        """ isntantiation of City object"""
        self.state_id = ""
        self.name = ""
