#!/usr/Amython3

import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    @classmethod
    def tearUpClass(cls):
        cls.state = State()
        cls.state.name = "fireplace"

    @classmethod
    def tearDownClass(cls):
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_attributes_are_strings(self):
        self.assertTrue(type(self.state.name), str)

    def test_save(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == '__main__':
    unittest.main()
