#!/usr/bin/python3
import datetime
import unittest

from models import storage

"""
This module Runs Tests Against the BaseModel Class
"""


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.BaseModel = __import__('models').base_model.BaseModel

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        del self.b0
        del self.BaseModel

    def test_object_isinstanceofBaseModel(self):
        """Tests if object is an instastance of BaseModel Class"""
        self.b0 = self.BaseModel()
        self.assertIsInstance(self.b0, self.BaseModel)

    def test_default_object_attributes_and_types(self):
        """Tests attributes value for instance of a BaseModel class."""
        self.b0 = self.BaseModel()
        attributes = storage.attributes()["BaseModel"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(self.b0, k))
            self.assertEqual(type(getattr(self.b0, k, None)), v)

    def test_instantiation_with_args_param(self):
        """ Tests when multiple args are passed to BaseModel __init__ method"""
        # No error should be reported
        self.b0 = self.BaseModel([x for x in range(200)])
        self.b0 = self.BaseModel(3,5,5,34,234)


    def generate_key_value_pairs(self):
        """ Generates a zipped pair of 2 arrays

                    Args:
                        None
                    Returns:
                         tuple(int,int): a tuple of two integer lists
                """
        key = [i for i in range(200)]
        val = [i for i in range(200)]
        return (key,val)

    def test_instantiation_with_kwargs_param(self):
        """
        Tests if instantiations of Basemodel with a Dict is properly handled
        :return:
        """

        key,val = self.generate_key_value_pairs()
        zip_content = zip([str(i) for i in key] ,val)
        my_dict = dict(zip_content)
        self.b0 = self.BaseModel(**my_dict)
        # print(self.b0)
        key = "{}.{}".format(type(self.b0).__name__, self.b0.id)
        check_dict = self.b0.to_dict()
        # print(check_dict)
        self.assertEqual(check_dict.get('1',None),1)
        self.assertEqual(check_dict.get('66',None),66)


    def test_each_run_a_unique_id_is_generated(self):
        "Checks that on each run a unique object ID is generated "
        self.b0 = None
        l = [self.BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(l)), len(l))

    def test_date_is_current(self):
        """
        Verify creation_date and update_date are recent
        :return:
        """
        date_now = datetime.datetime.now()
        self.b0 = self.BaseModel()
        diff = self.b0.updated_at - self.b0.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = self.b0.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)
    @unittest.skip("Not yet Implemented")
    def test_restored_obj_have_same_id(self):

        pass

    def test_to_dict_method(self):
        """Tests the public instance method to_dict()."""

        self.b0 = self.BaseModel()
        self.b0.age = 32

        obj_dict = self.b0.to_dict()
        self.assertEqual(obj_dict["id"], self.b0.id)
        self.assertEqual(obj_dict["__class__"], type(self.b0).__name__)
        self.assertEqual(obj_dict["created_at"], self.b0.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], self.b0.updated_at.isoformat())
        self.assertEqual(obj_dict["age"], self.b0.age)

    @unittest.skip("Not yet Implemented")
    def test_save_method(self):
        pass


    if __name__ == "__main__":
        unittest.main()
