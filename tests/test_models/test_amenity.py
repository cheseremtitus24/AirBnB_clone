#!/usr/Amython3

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    @classmethod
    def tearUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "fireplace"

    @classmethod
    def tearDownClass(cls):
        if (cls.amenity):
            del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.amenity.name), str)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == '__main__':
    unittest.main()
