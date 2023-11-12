#!/usr/bin/python3

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests FIleStorage class"""

    def setUp(self):
        self.instances = [
            BaseModel(), User(), State(),
            City(), Amenity(), Place(), Review()
            ]

        self.f_storage = FileStorage()

    def test_file_storage_init(self):
        "test initialization"

        self.assertIsInstance(self.f_storage, FileStorage)

    def test_all(self):
        "all return value"
        self.assertIsInstance(self.f_storage.all(), dict)

    def test_new(self):
        "tests if new adds an obj into __objects"

        for obj in self.instances:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)

            self.f_storage.new(obj)

            self.assertTrue(key in self.f_storage.all())

    def test_save(self):
        "save method testing"

        try:
            self.f_storage.save()
            with open("file.json", "r") as file:
                file_cont1 = json.load(file)
            self.f_storage.new(BaseModel())
            self.f_storage.save()
            with open("file.json", "r") as file:
                file_cont2 = json.load(file)

            self.assertFalse(file_cont1 == file_cont2)

            self.f_storage.save()
            with open("file.json", "r") as file:
                file_cont3 = json.load(file)

            self.assertTrue(file_cont2 == file_cont3)

        except FileNotFoundError as e:
            self.assertTrue(e is FileNotFoundError)

    def test_reload(self):
        try:
            self.f_storage.save()

            self.f_storage.new(Amenity())
            dict_current = self.f_storage.all()

            self.f_storage.reload()

            self.assertFalse(dict_current != self.f_storage.all())

        except FileNotFoundError as e:
            self.assertTrue(e is FileNotFoundError)
