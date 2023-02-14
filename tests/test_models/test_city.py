#!/usr/Cityython3

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.city = City()
        cls.city.name = "uganda kasese"
        cls.city.state_id = 'banga'

    @classmethod
    def tearDownClass(cls):
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.city.name), str)
        self.assertTrue(type(self.city.state_id), str)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == '__main__':
    unittest.main()
