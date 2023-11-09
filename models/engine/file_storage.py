#!/usr/bin/python3
import json


class FileStorage:
    """
    serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __object"""
        return self.__objects

    def new(self, obj):
        """sets an object in the dictionary with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes json file to object"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as file:
                d_instances = json.load(file)

            for key in d_instances:
                obj_name = d_instances[key]['__class__']
                obj_attr = d_instances[key]

                self.__objects[key] = eval(
                        "{}(**{})".format(obj_name, obj_attr)
                        )
        except FileNotFoundError:
            return
