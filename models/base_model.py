import uuid
from datetime import datetime
from models import storage
'''
defines the class baseModel for our instances
'''


class BaseModel:
    '''class BaseModel'''

    def __init__(self, *args, **kwargs):

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
        # should print in format [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dicts = self.__dict__.copy()
        dicts['__class__'] = (self.__class__.__name__)
        dicts['created_at'] = self.created_at.isoformat()
        dicts['updated_at'] = self.updated_at.isoformat()
        return dicts
