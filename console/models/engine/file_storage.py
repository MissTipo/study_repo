#!/usr/bin/python3
import json
from models.base_model import BaseModel
#import models

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            new_dict = FileStorage.__objects.copy()
            #from models.base_model import BaseModel
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                #from models.base_model import BaseModel
                new_obj = json.load(file)
                for key in new_obj.values():
                    name = key["__class__"]
                    del key["__class__"]
                    #print(key)
                    #from models.base_model import BaseModel
                    self.new(eval(name)(**key))

        except FileNotFoundError:
            return
