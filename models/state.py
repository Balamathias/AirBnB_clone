#!/usr/bin/python3
"""Module for State class."""
# from models.base_model import BaseModel


# class State(BaseModel):
#     """State class inherits from BaseModel."""

#     name = ""

#     @classmethod
#     def all(cls):
#         from models import storage
#         """Returns a dictionary of all instances of the class."""
#         return storage.all(cls)

from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for State"""
        super().__init__(*args, **kwargs)
