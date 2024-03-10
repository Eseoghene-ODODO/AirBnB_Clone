#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class body"""
    def __init__(self, *args, **kwargs):
        """Initializing User instance with public class attribute"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
