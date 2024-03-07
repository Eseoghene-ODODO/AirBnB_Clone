#!/usr/bin/python3
"""
My base model class
"""

import uuid
from datetime import datetime


class BaseModel:
    """class body"""

    def __init__(self, *args, **kwargs):
        """Initializing public instance attribute"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if 'self.created_at' in kwargs:
                    self.created_at = datetime.strptime(
                            kwargs['created_at'], "%Y-%m-%daT%H:%M:%S.%f"
                            )
                if 'self.updated_at' in kwargs:
                    self.updated_at = datetime.strptime(
                            kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
                            )
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of classname, the id and the dict
        """
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        """updates the public instance attribute with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
