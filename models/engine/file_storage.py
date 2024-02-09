#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Handles serialization and deserialization of objects to/from JSON."""

    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "State": State, "City": City,
                 "Amenity": Amenity, "Place": Place, "Review": Review}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    
    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objects, f)


    def reload(self):
        """Load objects from the JSON file."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    cls_name = obj_dict['__class__']
                    del obj_dict['__class__']
                    obj = FileStorage.__objects[cls_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
