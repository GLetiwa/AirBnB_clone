#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Has test cases for the BaseModel class and all it's instances"""
    def setUp(self):
        # Creates an instance of the BaseModel for testing
        self.model = BaseModel()

    def test_attributes(self):
        # Ensures that the BaseModel instance has the expected attributes
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        # Tests if id is generated and is unique for different instances
        other_model = BaseModel()
        self.assertNotEqual(self.model.id, other_model.id)

    def test_created_at_type(self):
        # Test if created_at is an instance of datetime
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        # Test if updated_at is an instance of datetime
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        # Test if the __str__ method produces the expected string representation
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method_updates_updated_at(self):
        # Test if calling save updates the updated_at attribute
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        # Test if the to_dict method returns a dictionary with expected keys/values
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)

    def test_id_is_string(self):
        # Test if the id attribute is a string
        self.assertIsInstance(self.model.id, str)

    def test_to_dict_includes_class_name(self):
        # Test if the to_dict method includes the __class__ key with the correct class name
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        model_dict = self.model.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(model_dict['created_at'], expected_format), self.model.created_at)
        self.assertEqual(datetime.strptime(model_dict['updated_at'], expected_format), self.model.updated_at)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.model.created_at, self.model.updated_at)

    """
    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.model.save()
        self.assertEqual(self.model.created_at, self.model.updated_at)
    """


if __name__ == '__main__':
    unittest.main()
