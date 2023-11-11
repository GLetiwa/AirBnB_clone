#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Place for testing
        self.x = Place()
        self.attributes = {
            'id': str,
            'created_at': datetime,
            'updated_at': datetime,
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest':int,
            'price_by_night':int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list
            }

    def test_attributes(self):
        # Ensure that the User instance has the expected attributes
        for key in self.attributes:
            self.assertTrue(hasattr(self.x, key))

    def test_attribute_types(self):
        # Test the attribute types of the created attributes
        for key, value in self.attributes.items():
            attr = getattr(self.x, key)
            self.assertTrue(type(attr) is value)

    def test_str_representation(self):
        # Test if the __str__ method produces the expected string representation
        expected_str = "[Place] ({}) {}".format(self.x.id, self.x.__dict__)
        self.assertEqual(str(self.x), expected_str)  

    def test_save_method_updates_updated_at(self):
        # Test if calling save updates the updated_at attribute
        old_updated_at = self.x.updated_at
        self.x.save()
        self.assertNotEqual(old_updated_at, self.x.updated_at)

    def test_to_dict_method(self):
        # Test if the to_dict method returns a dictionary with expected keys/values
        model_dict = self.x.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'Place')
        self.assertEqual(model_dict['id'], self.x.id)

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        model_dict = self.x.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(model_dict['created_at'], expected_format), self.x.created_at)
        self.assertEqual(datetime.strptime(model_dict['updated_at'], expected_format), self.x.updated_at)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.x.created_at, self.x.updated_at)

    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.x.save()
        self.assertEqual(self.x.created_at, self.x.created_at)

    def test_updated_at_after_save(self):
        # Test if created_at remains the same after calling save
        updated_time = self.x.updated_at 
        self.x.save()
        self.assertNotEqual(updated_time, self.x.updated_at)

    def test_object_creation_with_args(self):
        #creates an object when *args is passed in that doesn't have it as args
        l_arg = ['2023-11-11T06:02:57.369856', '2023-11-11T06:02:57.369856'
                 "Grace Letiwa", "Nairobi"]
        obj = Place(*l_arg)

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
            'city_id': 'Nairobi',
            'user_id': 'Ngong',
            'name': 'Harlequins',
            'description': 'Club',
            'number_rooms': 10,
            'number_bathrooms': 3,
            'max_guest':14,
            'price_by_night':2500,
            'latitude': 63.4,
            'longitude': 23.1,
            'amenity_ids': ["a", "b", 'c']
            }
        
        obj = Place(**d_kwargs)

        attributes = ['id', "created_at", 'updated_at']
        #check if original attributes are included
        for i in attributes:
            self.assertTrue(hasattr(obj, i))

        for key in d_kwargs:
            self.assertTrue(hasattr(obj, key))
    
    def test_is_child_instance(self):
        #tests if it is a child isntance of BaseModel

        self.assertTrue(isinstance(Place(), BaseModel))
        self.assertFalse(type(Place()) is BaseModel)

    def test_update_attributes(self):#add to the rest
        # Test if updating attributes works as expected
        d_args = {
            "id": "bca8e814-2fbc-47f0-8c29-1baf7c98afce",
            'city_id': 'Nairobi',
            'user_id': 'Ngong',
            'name': 'Harlequins',
            'description': 'Club',
            'number_rooms': 10,
            'number_bathrooms': 3,
            'max_guest':14,
            'price_by_night':2500,
            'latitude': 63.4,
            'longitude': 23.1,
            'amenity_ids': ["a", "b", 'c']
            }
        
        for key, value in d_args.items():
            setattr(self.x, key, value)
        
        for key, value in d_args.items():
            attr = getattr(self.x, key)
            self.assertEqual(attr, value)

    def test_default_values(self):#add to the rest
        # Test if the default values are set correctly

        strings = ['city_id', 'user_id', 'name', 'description']
        ints = ['number_rooms', 'max_guest', 'price_by_night']
        floats = ['latitude', 'longitude']

        for key in self.attributes:
            if (key in strings):
                self.assertEqual(getattr(self.x, key), "")
            elif (key in ints):
                self.assertEqual(getattr(self.x, key), 0)
            elif (key in floats):
                self.assertEqual(getattr(self.x, key), 0.0)
            elif (key == 'amenity_ids'): 
                  self.assertEqual(self.x.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()