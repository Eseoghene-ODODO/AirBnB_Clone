import unittest
from unittest.mock import patch
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.json'
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        result = self.file_storage.all()
        self.assertEqual(result, {})

    def test_new(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        result = self.file_storage.all()
        self.assertEqual(result, {'BaseModel.' + obj.id: obj})

    def test_save_and_reload(self):
        obj1 = BaseModel()
        obj2 = User()
        obj3 = Place()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.new(obj3)

        with patch('builtins.input', side_effect=['yes']):
            self.file_storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        result = new_storage.all()

        self.assertEqual(result, {
            'BaseModel.' + obj1.id: obj1,
            'User.' + obj2.id: obj2,
            'Place.' + obj3.id: obj3
        })

    def test_serialize_datetime(self):
        datetime_obj = BaseModel().created_at
        result = FileStorage.serialize_datetime(datetime_obj)
        self.assertEqual(result, datetime_obj.isoformat())

    def test_reload_nonexistent_file(self):
        self.assertFalse(os.path.exists(self.file_path))
        self.file_storage.reload()
        result = self.file_storage.all()
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
