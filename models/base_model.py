# models/base_model.py
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all AirBnB objects."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()  # Import storage from models module
    
    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return the string representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
