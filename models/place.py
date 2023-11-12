#!/usr/bin/python3


from models.base_model import BaseModel


class Place(BaseModel):
    """Place - Location object"""

    def __init__(self, *args, **kwargs):
        """Initialization of child instance from BaseModel"""

        if (not kwargs):
            dict_args = {
                'city_id': "",
                'user_id': "",
                'name': "",
                'description': "",
                'number_rooms': 0,
                'number_bathrooms': 0,
                'max_guest': 0,
                'price_by_night': 0,
                'latitude': 0.0,
                'longitude': 0.0,
                'amenity_ids': []
                }

            for key, value in dict_args.items():
                setattr(self, key, value)

        super().__init__(*args, **kwargs)
