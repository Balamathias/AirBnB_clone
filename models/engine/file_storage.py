#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Handles serialization and deserialization of objects to and from a JSON file.
    """

    # Class attributes
    __file_path = "file.json"
    __objects = {}

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and saves the objects dictionary to a JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file, default=lambda obj: obj.to_dict())

    def reload(self):
        """
        Deserializes and reloads objects from the JSON file into the objects dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_obj = self.CLASSES.get(class_name, BaseModel)
                obj = class_obj(**obj_data)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    @staticmethod
    def serialize(obj_dict):
        """
        Serializes the given objects dictionary to a JSON file.

        Args:
            obj_dict: The dictionary of objects to be serialized.
        """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file, default=lambda obj: obj.to_dict())

    @staticmethod
    def deserialize(json_obj):
        """
        Deserializes a JSON file to an objects dictionary.

        Args:
            json_obj: The JSON object to be deserialized.

        Returns:
            dict: The deserialized objects dictionary.
        """
        objects = {}
        if json_obj:
            for key, value in json_obj.items():
                class_name = value.get('__class__')
                class_obj = FileStorage.CLASSES.get(class_name, BaseModel)
                obj = class_obj(**value)
                objects[key] = obj
        return objects
