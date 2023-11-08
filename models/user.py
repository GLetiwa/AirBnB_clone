#!/usr/bin/python3
"""class user that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from Basemodel
    Has specified attributes; email, password, first name & last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
