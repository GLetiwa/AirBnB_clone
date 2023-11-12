#!/usr/bin/python3
"""class user that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from Basemodel
    Has specified attributes; email, password, first name & last name
    """
    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""


        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
