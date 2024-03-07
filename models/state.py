#!/usr/bin/python3
"""
class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class body"""
    def __init__(self):
        """Initializing public class attributes"""
        super().__init__()
        self.name = ""
