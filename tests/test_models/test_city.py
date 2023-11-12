#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
"Contains City Tests"


class TestCity(unittest.TestCase):
    """Has test cases for the City class"""

    def setUp(self):
        # Creates an instance of City for testing
        self.city = City()
        self.attributes = {'id': str,
                           'created_at': datetime,
                           'updated_at': datetime,
                           'state_id': str,
                           'name': str
                           }

    def test_attributes(self):
        # Ensures that the City instance has the expected attributes
        for key in self.attributes:
            self.assertTrue(hasattr(self.city, key))

    def test_attribute_types(self):
        # Test the attribute types of the created attributes
        for key, value in self.attributes.items():
            attr = getattr(self.city, key)
            self.assertTrue(type(attr) is value)

    def test_str_representation(self):
        # Test if __str__ produces the expected string representation
        expected_str = "[City] ({}) {}".format(
                self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method_updates_updated_at(self):
        # Test if calling save updates the updated_at attribute
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        # Test if to_dict returns a dictionary with expected keys/values
        model_dict = self.city.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'City')
        self.assertEqual(model_dict['id'], self.city.id)

    def test_to_dict_includes_class_name(self):
        # Test if to_dict includes the class_ key with the correct class name
        model_dict = self.city.to_dict()
        self.assertEqual(model_dict['__class__'], 'City')

    def test_to_dict_datetime_format(self):
        # Test if to_dict formats datetime attributes correctly
        model_dict = self.city.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(model_dict['created_at'], expected_format), self.city.created_at)
        self.assertEqual(datetime.strptime(model_dict['updated_at'], expected_format), self.city.updated_at)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.city.created_at, self.city.updated_at)

    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.city.save()
        self.assertEqual(self.city.created_at, self.city.created_at)

    def test_updated_at_after_save(self):
        # Test if created_at remains the same after calling save
        updated_time = self.city.updated_at
        self.city.save()
        self.assertNotEqual(updated_time, self.city.updated_at)

    def test_object_creation_with_args(self):
        # creates object when args is passed in that doesn't have it as args
        l_arg = ['2023-11-11T06:02:57.369856', '2023-11-11T06:02:57.369856'
                 "Grace Letiwa", "Nairobi"]
        obj = City(*l_arg)

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
            "__class__": 'City',
            "name": "Grace Letiwa",
            "state_id": "Nairobi"
            }

        obj = City(**d_kwargs)

        attributes = ['id', "created_at", 'updated_at']
        # check if original attributes are included
        for i in attributes:
            self.assertTrue(hasattr(obj, i))

        for key in d_kwargs:
            self.assertTrue(hasattr(obj, key))

    def test_is_child_instance(self):
        # tests if it is a child isntance of BaseModel

        self.assertTrue(isinstance(City(), BaseModel))
        self.assertFalse(type(City()) is BaseModel)

    def test_update_attributes(self):
        # Test if updating attributes works as expected
        d_args = {
            "id": "bca8e814-2fbc-47f0-8c29-1baf7c98afce",
            'state_id': 'Nairobi',
            'user_id': 'Ngong',
            'name': 'Harlequins',
            }

        for key, value in d_args.items():
            setattr(self.city, key, value)

        for key, value in d_args.items():
            attr = getattr(self.city, key)
            self.assertEqual(attr, value)

    def test_default_values(self):
        # Test if the default values are set correctly

        strings = ['state_id', 'name']

        for key in self.attributes:
            if (key in strings):
                self.assertEqual(getattr(self.city, key), "")


if __name__ == '__main__':
    unittest.main()
