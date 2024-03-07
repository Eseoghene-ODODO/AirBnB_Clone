#!/usr/bin/python3
"""
class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class body"""
    def __init__(self):
        """Initailizing public class attributes"""
        super().__init__()
        self.name = ""
