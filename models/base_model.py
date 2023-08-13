#!/usr/bin/env python3
'''
defines the class baseModel for our instances
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''class BaseModel'''

    def __init__(self, *args, **kwargs):
        '''initializes the class BaseModel'''
        for key, value in kwargs.items():
            if key != "__class__":
                if key == 'created_at' or key == 'updated_at':
                    d_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, d_format))
                elif key == 'id':
                    setattr(self, key, str(value))
                else:
                    setattr(self, key, value)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''should print in format [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at
          with the current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of
          __dict__ of the instance'''
        dicts = self.__dict__.copy()
        dicts['__class__'] = (self.__class__.__name__)
        dicts['created_at'] = self.created_at.isoformat()
        dicts['updated_at'] = self.updated_at.isoformat()
        return dicts
