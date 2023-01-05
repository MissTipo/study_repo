#!/usr/bin/python3
"""
"""
from uuid import uuid4
from datetime import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict


name = BaseModel()
# print(name.__str__())
print(BaseModel.to_dict(name))
