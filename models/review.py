#!/usr/bin/env python3
"""
A Review definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ a Review class definition that inherits
    from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
