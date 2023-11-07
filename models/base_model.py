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
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            iso_time = datetime.isoformat((datetime.now()))
            self.created_at = self.updated_at = iso_time
            # updated_at should be modified anytime we make a change in the object

    def __str__(self):
        """
            Prints ,class name. id & dict in human readable format
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            Public method
            - Updates the attr 'updated_at' with the current datetime
        """
        self.updated_at = datetime.isoformat(datetime.now())

    def to_dict(self):
        """
            Public method
            - returns a dictionary containing all keys & values of __dict__
            - also includes a new '__class__' key with class name
        """
        result_dict = dict(self.__dict__)
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return (result_dict)
        #new_dict = self.__dict__
        #new_dict['__class__'] = Rectangle.class_name()
        #return (new_dict)

    #@classmethod
    #def class_name(cls):
        """
            class method
            - Returns the class name
            - if you can find a better way to go about this
                by all means please do, and then share the procedure
                cause hapa nafloat mbaya
    """
        #return (cls.__name__)
