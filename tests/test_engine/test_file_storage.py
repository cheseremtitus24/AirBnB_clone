#!/usr/bin/python3
'''
Module test_file_storage
Defines Unittests for class FileStorage
'''
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''
    test file_storage methods
    '''
    @classmethod
    def setUpClass(cls):
        '''Run before other tests'''
        cls.city1 = City()
        cls.city1.state_id = 'kings'
        cls.city1.name = 'Kampala'

    @classmethod
    def tearDownClass(cls):
        '''
        Run after each test
        '''
        del cls.city1

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all(self):
        '''
        Tests method all'''
        storage = FileStorage()
        all_instances = storage.all()
        self.assertIsNotNone(all_instances)
        self.assertEqual(type(all_instances), dict)
        self.assertIs(all_instances, storage.__objects)

    def test_new(self):
        """
        Tests method: saves new obj into dictionary
        """
        storage = FileStorage()
        all_instances = storage.all()
        benon = User()
        benon.name = 'Benon'
        benon.id = '3333'
        storage.new(benon)
        key = benon.__class__.__name__ + "." + str(benon.id)
        self.assertIsNone(all_instances[key])

    def test_reload(self):
        """
        Tests method reload
        """
        storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as file:
            file.write("{}")
        with open("file.json", "r") as written_file:
            for line in written_file:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
