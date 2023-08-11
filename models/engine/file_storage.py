import json
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {} # contain key:value, key is Basemodel.class_id, value is The object itself i.e the instance

    def all(self):
        """returns dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict() # keys are basemodel.id and value is a dictionary
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(save_obj, f)
    
    def classes(self):
        """
        Creates a dict of all valid classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        return classes
    
    def reload(self):
        from models.base_model import BaseModel
        '''deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file \ 
            doesn’t exist, no exception should be raised)'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = BaseModel(**value)                                                                              
        except FileNotFoundError:
            pass
    
    def attr(self):
        attr = {
            "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
            "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name":str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                    "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id":str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
            "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
        }
        return attr
