import uuid
import datetime
from models import storage
'''
defines the class baseModel for our instances
'''


class BaseModel:
    '''class BaseModel'''

    def __init__(self, *args, **kwargs):
        if kwargs is None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.date.fromisoformat(value)
                if key == 'updated_at':
                    self.updated_at = datetime.date.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.save()
            storage.new(self)

    def __str__(self):
        # should print in format [<class name>] (<self.id>) <self.__dict__>
        return "{} ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dicts = self.__dict__
        dicts['__class__'] = (self.__class__.__name__)
        dicts['created_at'] = self.created_at.isoformat()
        dicts['updated_at'] = self.updated_at.isoformat()
        return (dicts)
