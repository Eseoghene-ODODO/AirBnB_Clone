#!/usr/bin/python3
"""
creating a unique FileStorage instance for my project
"""

from .base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


storage = FileStorage()
storage.reload()
