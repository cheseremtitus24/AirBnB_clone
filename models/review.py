#!/usr/bin/python3
'''
Module review
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Inherits from BaseModel
    Public atrr:
        place_id : will be Place.id
        user_id: will be User.id
        text
    '''
    place_id = ''
    user_id = ''
    text = ''
