import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        # serializer
        for k, v in self.__objects.items():
            with open(self.__file_path, 'w') as f:
                f.write(json.dumps(self.__objects[k]))

    def reload(self):
        # deserializer
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
        except:
            pass
