#!/usr/bin/python3
"""Module for State class."""
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """State class inherits from BaseModel."""

    name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all instances of the class."""
        return storage.all(cls)
