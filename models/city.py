#!/usr/bin/python3
"""Module for City class."""
# from models.base_model import BaseModel


# class City(BaseModel):
#     """City class inherits from BaseModel."""

#     state_id = ""
#     name = ""

#     @classmethod
#     def all(cls):
#         from models import storage
#         """Returns a dictionary of all instances of the class."""
#         return {obj.id: obj for obj in storage.all().values() if isinstance(obj, cls)}

from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for City"""
        super().__init__(*args, **kwargs)


