import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        # serializer
        for k, v in self.__objects.items():
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                d = {k: v.to_dict() for k, v in self.__objects.items()}
                json.dump(d, f)

    def reload(self):
        # deserializer
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.loads(f.read())
        except:
            return
