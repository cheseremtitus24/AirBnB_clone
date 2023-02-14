#!/usr/bin/python3

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amenitys = Amenity()
        cls.amenitys.name = "uganda kasese"

    @classmethod
    def tearDownClass(cls):
        del cls.amenitys
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenitys.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.amenitys.__dict__)
        self.assertTrue('created_at' in self.amenitys.__dict__)
        self.assertTrue('updated_at' in self.amenitys.__dict__)
        self.assertTrue('id' in self.amenitys.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.amenitys.name), str)

    def test_save(self):
        self.amenitys.save()
        self.assertNotEqual(self.amenitys.created_at, self.amenitys.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenitys), True)


if __name__ == '__main__':
    unittest.main()
