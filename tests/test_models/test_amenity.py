# !/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
"Contains Amenity Tests"


class TestAmenity(unittest.TestCase):
    """Has test cases for the Amenity class"""

    def setUp(self):
        """Creates an instance of Amenity for testing"""
        self.amenity = Amenity()
        self.attributes = {'id': str,
                           'created_at': datetime,
                           'updated_at': datetime,
                           'name': str
                           }

    def test_attributes(self):
        """Ensures that the Amenity instance has the expected attributes"""
        for key in self.attributes:
            self.assertTrue(hasattr(self.amenity, key))

    def test_attribute_types(self):
        """Test the attribute types of the created attributes"""
        for key, value in self.attributes.items():
            attr = getattr(self.amenity, key)
            self.assertTrue(type(attr) is value)

    def test_str_representation(self):
        """Test if the __str__ method produces  expected string"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method_updates_updated_at(self):
        """Test if calling save updates the updated_at attribute"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns expected dictionary"""
        model_dict = self.amenity.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'Amenity')
        self.assertEqual(model_dict['id'], self.amenity.id)

    def test_to_dict_includes_class_name(self):
        """Test if to_dict method includes \
            _class__ key with the correct class name"""
        model_dict = self.amenity.to_dict()
        self.assertEqual(model_dict['__class__'], 'Amenity')

    def test_to_dict_datetime_format(self):
        """Test if the to_dict method formats datetime attributes correctly"""
        model_dict = self.amenity.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(
            datetime.strptime(
                model_dict['created_at'], expected_format
                ), self.amenity.created_at)
        self.assertEqual(
            datetime.strptime(
                model_dict['updated_at'], expected_format
                ), self.amenity.updated_at)

    def test_created_at_before_save(self):
        """Test if created_at before calling save"""
        self.assertEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_created_at_after_save(self):
        """Test if created_at remains the same after calling save"""
        self.amenity.save()
        self.assertEqual(self.amenity.created_at, self.amenity.created_at)

    def test_updated_at_after_save(self):
        """Test if created_at remains the same after calling save"""
        updated_time = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(updated_time, self.amenity.updated_at)

    def test_object_creation_with_args(self):
        """creates an object when *args is passed"""
        l_arg = ['2023-11-11T06:02:57.369856', '2023-11-11T06:02:57.369856'
                 "Grace Letiwa"]
        obj = Amenity(*l_arg)

        for key in self.attributes:
            self.assertTrue(hasattr(obj, key))

        for i in l_arg:
            self.assertNotEqual(i, obj.id)
            self.assertNotEqual(i, obj.updated_at)
            self.assertNotEqual(i, obj.created_at)

        del obj

    def test_object_creation_with_kwargs_complete(self):
        """creates an object when *kwargs is passed in"""

        d_kwargs = {
            "id": "bca8e814-2fbc-47f0-8c29-1baf7c98afce",
            "created_at": "2023-11-09T09:54:01.928417",
            "updated_at": "2023-11-09T09:54:01.928417",
            "name": "Grace Letiwa",
            "state_id": "Nairobi"
            }

        obj = Amenity(**d_kwargs)

        attributes = ['id', "created_at", 'updated_at']
        # check if original attributes are included
        for i in attributes:
            self.assertTrue(hasattr(obj, i))

        for key in d_kwargs:
            self.assertTrue(hasattr(obj, key))

    def test_is_child_instance(self):
        """tests if it is a child isntance of BaseModel"""

        self.assertTrue(isinstance(Amenity(), BaseModel))
        self.assertFalse(type(Amenity()) is BaseModel)

    def test_default_values(self):
        """Test if the default values are set correctly"""

        self.assertEqual(getattr(self.amenity, 'name'), "")

    def test_update_attributes(self):
        """Test if updating attributes works as expected"""
        setattr(self.amenity, 'name', 'Letiwa')
        self.assertEqual(self.amenity.name, 'Letiwa')
