#!/usr/bin/python3

import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Place for testing
        self.place = Place()

    def test_attributes(self):
        # Ensure that the Place instance has the expected attributes
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_default_values(self):
        # Test if the default values are set correctly
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict_method(self):
        # Test if the to_dict method returns a dictionary with expected keys/values
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.place.created_at, self.place.updated_at)

    """
    def test_created_at_after_save(self):
        # Test if created_at remains the same after calling save
        self.place.save()
        self.assertEqual(self.place.created_at, self.place.updated_at)
    """

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        place_dict = self.place.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(place_dict['created_at'], expected_format), self.place.created_at)
        self.assertEqual(datetime.strptime(place_dict['updated_at'], expected_format), self.place.updated_at)

    def test_attribute_types(self):
        # Test the attribute types
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    """
    def test_negative_values(self):
        # Test if negative values for certain attributes are handled correctly
        self.place.number_rooms = -1
        self.assertEqual(self.place.number_rooms, 0)

    def test_large_values(self):
        # Test if large values for certain attributes are handled correctly
        self.place.max_guest = 1000000
        self.assertEqual(self.place.max_guest, 0)
    """


if __name__ == '__main__':
    unittest.main()
