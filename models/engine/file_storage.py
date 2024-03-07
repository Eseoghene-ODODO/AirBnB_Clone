#!/usr/bin/python3
"""
A FileStorage class the serializes/desserializes instances to JSON file
"""

from models.base_model import BaseModel
import json
from datetime import datetime
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """class body"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of the private class attribute __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """method(new) body"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """serializes __objects to json"""
        serialized_objs = {}
        for key, obj in self.__class__.__objects.items():
            serialized_objs[key] = obj.__dict__
        with open(self.__class__.__file_path, "w", encoding='utf-8') as file:
            json.dump(serialized_objs, file, default=self.serialize_datetime)

    @staticmethod
    def serialize_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj

    def reload(self):
        """desrializes json to objects"""
        try:
            with open(
                    self.__class__.__file_path, "r", encoding='utf-8'
                    ) as file:
                data = json.load(file)  # data is handling deserialization
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    new_obj = obj_class(**value)
                    self.__class__.__objects[key] = new_obj
        except (FileNotFoundError, json.JSONDecodeError):
            pass
if __name__ == '__main__':
    storage = FileStorage()
    storage.reload()
