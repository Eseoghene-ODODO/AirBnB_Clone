#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances
"""

from models.base_model import BaseModel
import json
from os.path import exists
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class body"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = None  # Initialize obj here
                    if class_name == 'State':
                        obj = State(**obj_dict)
                    elif class_name == 'City':
                        obj = City(**obj_dict)
                    elif class_name == 'Amenity':
                        obj = Amenity(**obj_dict)
                    elif class_name == 'Place':
                        obj = Place(**obj_dict)
                    elif class_name == 'Review':
                        obj = Review(**obj_dict)
                    elif class_name == 'BaseModel':
                        obj = BaseModel(**obj_dict)
                    else:
                        obj = BaseModel(**obj_dict)
                    self.__objects[key] = obj
