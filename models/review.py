#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """Review - Rating class"""

    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
