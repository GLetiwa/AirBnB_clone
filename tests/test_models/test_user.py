#!/usr/bin/python3

import unittest

from datetime import datetime
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        # Create an instance of the User for testing
        self.user = User()
        self.attributes = {'id': str,
                           'created_at': datetime,
                           'updated_at': datetime,
                           'email': str,
                           'password': str,
                           'first_name': str,
                           'last_name': str
                           }

    def test_attributes(self):
        # Ensure that the User instance has the expected attributes
        for key in self.attributes:
            self.assertTrue(hasattr(self.user, key))

    def test_attribute_types(self):
        # Test the attribute types of the created attributes
        for key, value in self.attributes.items():
            attr = getattr(self.user, key)
            self.assertTrue(type(attr) is value)

    def test_str_representation(self):
        # Test if __str__ produces the expected string representation
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        # Test if to_dict returns a dictionary with expected keys/values
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)

    def test_to_dict_includes_class_name(self):
        # Test if to_dict includes the class key with the correct class name
        model_dict = self.user.to_dict()
        self.assertEqual(model_dict['__class__'], 'User')

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        model_dict = self.user.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(model_dict['created_at'], expected_format), self.user.created_at)
        self.assertEqual(datetime.strptime(model_dict['updated_at'], expected_format), self.user.updated_at)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.user.save()
        self.assertEqual(self.user.created_at, self.user.created_at)

    def test_updated_at_after_save(self):
        # Test if created_at remains the same after calling save
        updated_time = self.user.updated_at
        self.user.save()
        self.assertNotEqual(updated_time, self.user.updated_at)

    def test_object_creation_with_args(self):
        # creates an object when args is passed in that doesn't have it as args
        l_arg = ['2023-11-11T06:02:57.369856', '2023-11-11T06:02:57.369856'
                 "Grace", "Letiwa", "letiwa@softwareengineer" "Nairobi"]
        obj = User(*l_arg)

        for key in self.attributes:
            self.assertTrue(hasattr(obj, key))

        for i in l_arg:
            self.assertNotEqual(i, obj.id)
            self.assertNotEqual(i, obj.updated_at)
            self.assertNotEqual(i, obj.created_at)

        del obj

    def test_object_creation_with_kwargs_complete(self):
        # creates an object when *kwargs is passed in

        d_kwargs = {
            "id": "bca8e814-2fbc-47f0-8c29-1baf7c98afce",
            "created_at": "2023-11-09T09:54:01.928417",
            "updated_at": "2023-11-09T09:54:01.928417",
            'email': 'letiwa@softwareengineer',
            'password': "123456",
            'first_name': 'Grace',
            'last_name': 'Letiwa'
            }

        obj = User(**d_kwargs)

        attributes = ['email', 'password', 'first_name', 'last_name']
        # check if original attributes are included
        for i in attributes:
            self.assertTrue(hasattr(obj, i))

        for key in d_kwargs:
            self.assertTrue(hasattr(obj, key))

    def test_is_child_instance(self):
        # tests if it is a child isntance of BaseModel

        self.assertTrue(isinstance(User(), BaseModel))
        self.assertFalse(type(User()) is BaseModel)

    def test_update_attributes(self):
        # Test if updating attributes works as expected
        d_args = {
            'email': "test@example.com", 'password': "password123",
            'first_name': "Steve", 'last_name': "Tony"
            }

        for key, value in d_args.items():
            setattr(self.user, key, value)

        for key, value in d_args.items():
            attr = getattr(self.user, key)
            self.assertEqual(attr, value)

    def test_default_values(self):
        # Test if the default values are set correctly
        for key in self.attributes:
            if key in ['email', 'password', 'first_name', 'last_name']:
                value = getattr(self.user, key)
                self.assertEqual(value, "")


if __name__ == '__main__':
    unittest.main()
