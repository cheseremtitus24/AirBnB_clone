#!/usr/bin/python3
"""
Module file_storage
Initilase class File Storage 
"""

from models.base_model import BaseModel
import json


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
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(my_dict, file)
                                               
    def reload(self):
        '''
        deserialise
        if json file exisists , convert json objects back to instances in a dictionary
        '''
        try:
            with open(self.__file_path, 'r') as file:
                new_obj = json.loads(file)
                for key, value in new_obj.items():
                    obj = self.class_dic[value['__class__']](**value)
                    self.__objects[key] = obj
        except FileExistsError:
            pass
        

