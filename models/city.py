#!/usr/bin/python3
'''
Module city
'''
from models.base_model import BaseModel

class City(BaseModel):
    '''
    Inherits from BaseModel
    Public atrr:
        state_id: will be State.id
        name
    '''
    state_id = ''
    name = ''