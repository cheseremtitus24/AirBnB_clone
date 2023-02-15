#!/usr/bin/python3

import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place = Place()
        cls.place.name = "uganda kasese"
        cls.place.city_id = "Benon"
        cls.place.user_id = "Masereka"
        cls.place.description = "good contion 3 rooms"
        cls.place.number_rooms = 2
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 3
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('id' in self.place.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.place.name), str)
        self.assertTrue(type(self.place.user_id), str)
        self.assertTrue(type(self.place.city_id), str)
        self.assertTrue(type(self.place.number_bathrooms), int)
        self.assertTrue(type(self.place.number_rooms), int)
        self.assertTrue(type(self.place.latitude), float)
        self.assertTrue(type(self.place.description), str)
        self.assertTrue(type(self.place.amenity_ids), list)
        self.assertTrue(type(self.place.price_by_night), int)
        self.assertTrue(type(self.place.max_quest), int)
        self.assertTrue(type(self.place.longitude), float)

    def test_save(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == '__main__':
    unittest.main()
