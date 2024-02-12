# #!/usr/bin/python3
"""Module for User class."""

from models.base_model import BaseModel
import models

class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method for User"""
        super().__init__(*args, **kwargs)
    
    # def update(self, attribute_dict):
    #     """
    #     Update the attributes of the user instance and save the change.
    #     """
    #     for key, value in attribute_dict.items():
    #         setattr(self, key, value)
    #     self.save()

    def update_attributes(self, attribute_dict):
        """
        Update the attributes of the user instance and save the change.
        """
        print(f"Updating attributes: {attribute_dict}")
        for key, value in attribute_dict.items():
            setattr(self, key, value)
        self.save()

    @classmethod
    def all(cls):
        return [obj for obj in models.storage.all().values() if isinstance(obj, cls)]
    
    @classmethod
    def count(cls):
        """
        Returns the number of instances of User currently in storage.
        """
        return len([obj for obj in models.storage.all().values() if isinstance(obj, cls)])


    



