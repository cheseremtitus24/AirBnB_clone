#!/usr/bin/python3

import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.states = State()
        cls.states.name = "uganda kasese"

    @classmethod
    def tearDownClass(cls):
        del cls.states
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.states.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.states.__dict__)
        self.assertTrue('created_at' in self.states.__dict__)
        self.assertTrue('updated_at' in self.states.__dict__)
        self.assertTrue('id' in self.states.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.states.name), str)

    def test_save(self):
        self.states.save()
        self.assertNotEqual(self.states.created_at, self.states.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.states), True)


if __name__ == '__main__':
    unittest.main()
