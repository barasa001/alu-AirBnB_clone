#!/usr/bin/python3
"""Our BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """contains common attribute"""
    def __init__self(self, *arg, **kwargs):
        if not kwargs:
            
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            f= "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        class_name = "[" + self.__class__.__name__ + "]"
        lst = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(lst)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
