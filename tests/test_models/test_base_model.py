#!/usr/bin/python3
import unittest

from models import storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        self.BaseModel = __import__('models').base_model.BaseModel
        self.City = __import__('models').city.City

    def tearDown(self):
        """
        These are module setUp
        Teardown Methods
        :return:
        """
        # del self.b0
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
        pass

    def test_instantiation_with_kwargs_param(self):
        pass


    def test_each_run_a_unique_id_is_generated(self):
        pass

    def test_date_is_current(self):
        """
        Verify creation_date and update_date are recent
        :return:
        """
        pass

    def test_restored_obj_have_same_id(self):
        pass




if __name__ == "__main__":
    unittest.main()
