#!/usr/bin/python3

import unittest
import os
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.first_name = "Benon"
        cls.user.last_name = "Masereka"
        cls.user.email = "benonk@mail.com"
        cls.user.password = "root"
    @classmethod
    def tearDownClass(cls):
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_has_attributes(self):
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
    
    def test_attributes_are_strings(self):
        self.assertTrue(type(self.user.email), str)
        self.assertTrue(type(self.user.first_name), str)
        self.assertTrue(type(self.user.password),str)
        self.assertTrue(type(self.user.last_name), str)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)
    
    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user), True)

if __name__ == '__main__':
    unittest.main()



