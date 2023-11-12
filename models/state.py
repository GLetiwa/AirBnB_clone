#!/usr/bin/python3
"""classes inheriting from Basemodel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State - State location object(bro idk either)"""

    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""

        if (not kwargs):
            self.name = ""
        super().__init__(*args, **kwargs)
