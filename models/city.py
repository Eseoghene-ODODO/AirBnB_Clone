#!/usr/bin/python3
"""
class City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class body"""
    def __init__(self):
        """Initializing the City public instance attribute"""
        super().__init__()
        self.state_id = ""
        self.name = ""
