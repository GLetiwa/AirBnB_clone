#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """Review - Rating class"""

    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""

        if (not kwargs):
            dict_args = {
                'place_id': "",
                'user_id': "",
                'text': ""
                }
            for key, value in dict_args.items():
                setattr(self, key, value)

        super().__init__(*args, **kwargs)
