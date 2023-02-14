#!/usr/Amython3

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    @classmethod
    def tearUpClass(cls):
        cls.review = Review()
        cls.review.place_id = 'school'
        cls.review.user_id = 'ee'
        cls.review.text = 'ee'

    @classmethod
    def tearDownClass(cls):
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.review.user_id), str)
        self.assertTrue(type(self.review.place_id), str)
        self.assertTrue(type(self.review.text), str)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == '__main__':
    unittest.main()
