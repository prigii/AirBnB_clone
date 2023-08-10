import json
import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        # serializer
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict()
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
        # deserializer
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                self.new(eval(key.split(".")[0])(**value))
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
