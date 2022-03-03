#!/usr/bin/env python3
"""
A Review definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ a Review class definition that inherits
    from BaseModel"""
    def __init__(self):
        """ a Review object instantiation"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
