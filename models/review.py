#!/usr/bin/python3
"""Module for Review class."""
# from models.base_model import BaseModel


# class Review(BaseModel):
#     """Review class inherits from BaseModel."""

#     place_id = ""
#     user_id = ""
#     text = ""

#     @classmethod
#     def all(cls):
#         from models import storage
#         """Returns a dictionary of all instances of the class."""
#         return storage.all(cls)


from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for Review"""
        super().__init__(*args, **kwargs)


