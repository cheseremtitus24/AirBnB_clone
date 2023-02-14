#!/usr/bin/python3

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reviews = Review()
        cls.reviews.text = "uganda kasese"
        cls.reviews.place_id = 'banga'
        cls.reviews.user_id = "masika"

    @classmethod
    def tearDownClass(cls):
        del cls.reviews
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.reviews.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('place_id' in self.reviews.__dict__)
        self.assertTrue('user_id' in self.reviews.__dict__)
        self.assertTrue('created_at' in self.reviews.__dict__)
        self.assertTrue('updated_at' in self.reviews.__dict__)
        self.assertTrue('id' in self.reviews.__dict__)
        self.assertTrue('text' in self.reviews.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.reviews.user_id), str)
        self.assertTrue(type(self.reviews.place_id), str)
        self.assertTrue(type(self.reviews.text), str)

    def test_save(self):
        self.reviews.save()
        self.assertNotEqual(self.reviews.created_at, self.reviews.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.reviews), True)


if __name__ == '__main__':
    unittest.main()
