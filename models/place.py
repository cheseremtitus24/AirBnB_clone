#!/usr/bin/python3
'''
Module place
'''
from models.base_model import BaseModel

class Place(BaseModel):
    '''
    Inherits from BaseModel
    Public atrr:
        name
        city_id : willbe City.id
        user_id : will be User.id
        description
        number_rooms
        number_bathrooms
        max_quest
        pricr_by_night
        latitude
        longitude
        amenity_ids
    '''
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_quest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''