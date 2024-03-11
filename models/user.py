#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class body"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
