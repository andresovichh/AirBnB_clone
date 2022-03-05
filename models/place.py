#!/usr/bin/env python3
"""
A Place definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ a class definition of Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    pice_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
