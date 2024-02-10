#!/usr/bin/python3
"""Module for Amenity class."""
# from models.base_model import BaseModel


# class Amenity(BaseModel):
#     """Amenity class inherits from BaseModel."""

#     name = ""

#     @classmethod
#     def all(cls):
#         from models import storage
#         """Returns a dictionary of all instances of the class."""
#         return storage.all(cls)

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for Amenity"""
        super().__init__(*args, **kwargs)


