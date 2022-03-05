#!/usr/bin/env python3
"""
A State definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """ A class State that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)