from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string datetime to datetime object
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    continue  # Skip __class__ when initializing attributes
                else:
                    setattr(self, key, value)
        else:
            # Create new instance with unique ID and current datetime
            self.id = str(uuid4.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add the new instance to storage
            from models import storage
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        # Call the save method of storage
        from models import storage
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
