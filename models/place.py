#!/usr/bin/python3
"""
class Place that inherites from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class body"""
    def __init__(self):
        """Initializing public class attributes"""
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
