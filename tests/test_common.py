import unittest
from datetime import datetime
from models.user import User
"""from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review"""
from models.base_model import BaseModel

class TestCommontests(unittest.TestCase):
    "TestCommontests - Tests common testcases"

    def test_instance_creation_empty(self):
        "Runs tests on empty instance creation"
        i = User()
        #for i in instances:
        #original attributes
        self.assertTrue(hasattr(i, 'id'))
        self.assertTrue(hasattr(i, 'created_at'))
        self.assertTrue(hasattr(i, 'updated_at'))

        #type original attributes
        self.assertTrue(i.updated_at, datetime)
        self.assertTrue(i.created_at, datetime)

        i2 = User()
        #id test
        self.assertNotEqual(i2.id, i.id)

        #created_at & updated_at
        self.assertNotEqual(i2.created_at, i.created_at)
        self.assertNotEqual(i2.updated_at, i.updated_at)

        #childprocess of BaseModel
        x = BaseModel()
        self.assertTrue(isinstance(i, BaseModel))
        self.assertFalse(type(i) == BaseModel)
        self.assertTrue(type(i) == User)

        #if childprocess and parent process have different attr
        self.assertNotEqual(x.id, i.id)

        #created_at & updated_at
        self.assertNotEqual(x.created_at, i.created_at)
        self.assertNotEqual(x.updated_at, i.updated_at)

        del i

    def test_common_methods(self):
        "Tests common method implementations"
        i = User()
        
        #for i in instances:
        # str method
        expected_str = "[{}] ({}) {}".format(i.__class__.__name__, i.id, i.__dict__)
        self.assertEqual(str(i), expected_str)

        #save method
        previous_time = i.updated_at
        creation_time = i.created_at
        i.save()
        # checks the change of updated time
        self.assertFalse(previous_time == i.updated_at)
        self.assertFalse(creation_time == i.updated_at)
        self.assertTrue(creation_time == i.created_at)
        # well also need to check that the file has been modified if it exists

        #to dict

        dict_attr = dict(i.__dict__)
        dict_attr['__class__'] = i.__class__.__name__
        dict_attr['created_at'] = datetime.isoformat(i.created_at)
        dict_attr['updated_at'] = datetime.isoformat(i.updated_at)

        i_dict = i.to_dict()

        #checks if created_at & updated_at serialize correctly
        self.assertTrue(dict_attr == i_dict)

        # checks if '__class__' in i_dict
        self.assertTrue('__class__' in i_dict.keys())

        for key,value in i_dict.items():
            if key == 'created_at' or key == 'updated_at':
                c_time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.assertTrue(type(c_time) == datetime)

        del i

    def test_method_errors(self):
        "Tests errors with methods"
