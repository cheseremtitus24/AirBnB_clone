#!/usr/bin/python3
"""
Module file_storage
Initilase class File Storage 
"""

import json

import models


class FileStorage:
    """
    serialises instances to a Json file and deserialises Json file to instances
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        Return dictionary of class.id: object instances"
        return a diction of clasess as keys and their instances as values
        """
        return self.__objects
    
    def new(self, obj):
        """
        add new objects to existing dictionaries
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serialise
        save obj dictioniries to json file
        """
        json_objs = {}
        for key, value in self.__objects.items():
            json_objs[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
                json.dump(json_objs, file)
                                               
    def reload(self):
        '''
        deserialise
        if json file exisists , convert json objects back to instances in a dictionary
        '''
        print("Debug: Loading File Objects from File storage")
        try:
            print("Searched file path is ", self.__file_path)
            with open(self.__file_path, 'r') as file:
                new_obj = json.load(file)
                for key in new_obj:
                    self.__objects[key] = getattr(models, new_obj[key]['__class__'])(**new_obj[key])
        except FileNotFoundError:
            print("Debug: The Requested Json File Does not Exist")
            pass
        

