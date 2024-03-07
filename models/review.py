#!/usr/bin/python3
"""
class Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class body"""
    def __init__(self):
        """Initializing public class attributes"""
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
