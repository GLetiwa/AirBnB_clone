#!/usr/bin/python3

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        # Create an instance of the User for testing
        self.user = User()

    def test_attributes(self):
        # Ensure that the User instance has the expected attributes
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        # Test if the default values are set correctly
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        # Test if the to_dict method returns a dictionary with expected keys/values
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)

    def test_created_at_before_save(self):
        # Test if created_at and updated_at are the same before calling save
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_datetime_format(self):
        # Test if the to_dict method formats datetime attributes correctly
        user_dict = self.user.to_dict()
        expected_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(datetime.strptime(user_dict['created_at'], expected_format), self.user.created_at)
        self.assertEqual(datetime.strptime(user_dict['updated_at'], expected_format), self.user.updated_at)

    def test_attribute_types(self):
        # Ensure that attributes have the correct types
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_update_attributes(self):
        # Test if updating attributes works as expected
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "Steve"
        self.user.last_name = "Tony"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "Steve")
        self.assertEqual(self.user.last_name, "Tony")


if __name__ == '__main__':
    unittest.main()
