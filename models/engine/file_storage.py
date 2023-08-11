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
        ''' serializes __objects to the JSON file (path: __file_path)'''
        save_obj = {}
        for key, value in self.__objects.items():
            # keys are basemodel.id and value is a dictionary
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
        '''deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists; otherwise, do nothing. If the file
            doesn’t exist, no exception should be raised)'''
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = self.classes(
                    )[value["__class__"]](**value)
        except FileNotFoundError:
            pass
