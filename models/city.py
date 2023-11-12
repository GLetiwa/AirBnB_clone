#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City - City location object"""

    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""

        if (not kwargs):
            self.state_id = ""
            self.name = ""
        super().__init__(*args, **kwargs)
