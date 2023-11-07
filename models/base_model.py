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

    def __init__(self):
        """
            - BaseModel object instantiation
            - Creates an instance of type 'BaseModel' with params
                - id - unique user id
                - created_at - time instance was created
                - updated_at - time when a change occurs in the instance
        """

        self.id = str(uuid.uuid4())
        iso_time = datetime.isoformat((datetime.now()))
        self.created_at = self.updated_at = iso_time
        # updated_at should be modified anytime we make a change in the object

    def __str__(self, name=None):
        """
            Prints ,class name. id & dict in human readable format
        """

        if (name is None):
            name = BaseModel.class_name()
        return (f'[{name}] ({self.id}) {self.__dict__}')

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

        new_dict = self.__dict__
        new_dict['__class__'] = Rectangle.class_name()
        return (new_dict)

    @classmethod
    def class_name(cls):
        """
            class method
            - Returns the class name
            - if you can find a better way to go about this
                by all means please do, and then share the procedure
                cause hapa nafloat mbaya
    """
        return (cls.__name__)
