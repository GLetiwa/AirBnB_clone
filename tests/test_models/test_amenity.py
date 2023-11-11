#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
"Contains Amenity Tests"

class TestAmenity(unittest.TestCase):
    """Has test cases for the Amenity class"""

    def setUp(self):
        # Creates an instance of Amenity for testing
        self.model = Amenity()
        self.attributes = {'id': str,
                           'created_at': datetime,
                           'updated_at': datetime,
                           'name': str
                           }

    def test_attributes(self):
        # Ensures that the Amenity instance has the expected attributes
        for key in self.attributes:
            self.assertTrue(hasattr(self.model, key))

    def test_attribute_types(self):
        # Test the attribute types of the created attributes
        for key, value in self.attributes.items():
            attr = getattr(self.model, key)
            self.assertTrue(type(attr) is value)

    def test_str_representation(self):
        # Test if the __str__ method produces the expected string representation
        expected_str = "[Amenity] ({}) {}".format(self.model.id, self.model.__dict__)
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
        self.assertEqual(model_dict['__class__'], 'Amenity')
        self.assertEqual(model_dict['id'], self.model.id)

    def test_to_dict_includes_class_name(self):
        # Test if the to_dict method includes the __class__ key with the correct class name
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'Amenity')

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        model_dict = self.model.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(model_dict['created_at'], expected_format), self.model.created_at)
        self.assertEqual(datetime.strptime(model_dict['updated_at'], expected_format), self.model.updated_at)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.model.save()
        self.assertEqual(self.model.created_at, self.model.created_at)

    def test_updated_at_after_save(self):
        # Test if created_at remains the same after calling save
        updated_time = self.model.updated_at 
        self.model.save()
        self.assertNotEqual(updated_time, self.model.updated_at)

    def test_object_creation_with_args(self):
        #creates an object when *args is passed in that doesn't have it as args
        l_arg = ['2023-11-11T06:02:57.369856', '2023-11-11T06:02:57.369856'
                 "Grace Letiwa"]
        obj = Amenity(*l_arg)

        for key in self.attributes:
            self.assertTrue(hasattr(obj,key))


        for i in l_arg:
            self.assertNotEqual(i, obj.id)
            self.assertNotEqual(i, obj.updated_at)
            self.assertNotEqual(i,obj.created_at)
        
        del obj
    
    def test_object_creation_with_kwargs_complete(self):
        #creates an object when *kwargs is passed in

        d_kwargs = {
            "id": "bca8e814-2fbc-47f0-8c29-1baf7c98afce",
            "created_at": "2023-11-09T09:54:01.928417",
            "updated_at": "2023-11-09T09:54:01.928417",
            "name": "Grace Letiwa",
            "state_id": "Nairobi"
            }
        
        obj = Amenity(**d_kwargs)

        attributes = ['id', "created_at", 'updated_at']
        #check if original attributes are included
        for i in attributes:
            self.assertTrue(hasattr(obj, i))

        for key in d_kwargs:
            self.assertTrue(hasattr(obj, key))
    
    def test_is_child_instance(self):
        #tests if it is a child isntance of BaseModel

        self.assertTrue(isinstance(Amenity(), BaseModel))
        self.assertFalse(type(Amenity()) is BaseModel)

