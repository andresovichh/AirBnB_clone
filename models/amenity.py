"""
A Amenity definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ a class definition of Amenity"""
    def __init__(self):
        """ an Amenity object instantiation"""
        self.name = ""
