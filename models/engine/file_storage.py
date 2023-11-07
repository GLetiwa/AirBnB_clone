#!/usr/bin/python3

import json

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __object"""
        return self.__object

    def new(self, obj):
        """sets and object in the dictionary with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        #craete a dictionary to hold serialized objects
        obj_dict = {key: obj.to_dict for key, obj in self.__object.items()}
        #open json file for writing
        with open (self.__file_path, "w", encoding='utf-8') as file:
            """write ob_dict to the file"""
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes json file to object"""
        try:
            with open(self.__file_path, "r") as file:
                d_instances = json.load(file)

            for key in d_instances:


        except FileNotFoundError:
            return

