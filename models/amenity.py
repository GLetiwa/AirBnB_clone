#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity - idk what this is so i'll leave this to you"""
    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""
        super().__init__(*args, **kwargs)
        self.name = ""
