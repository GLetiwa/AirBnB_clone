#!/usr/bin/python3
"""
    base_model.py
    - Module
    - Contains parent class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel():
    """
        BaseModel
        - Class object & base class
        - Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            - BaseModel object instantiation
            - Creates an instance of type 'BaseModel' with params
                - id - unique user id
                - created_at - time instance was created
                - updated_at - time when a change occurs in the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            iso_time = datetime.now()
            self.created_at = self.updated_at = iso_time
            # updated_at - modified anytime we make a change in the object

    def __str__(self):
        """
            Prints ,class name. id & dict in human readable format
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )

    def save(self):
        """
            Public method
            - Updates the attr 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Public method
            - returns a dictionary containing all keys & values of __dict__
            - also includes a new '__class__' key with class name
        """
        result_dict = dict(self.__dict__)
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = datetime.isoformat(self.created_at)
        result_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return (result_dict)
