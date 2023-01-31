#!/usr/bin/python3
"""Our BaseModel that defines all common attributes/methods for other classes
"""

from datetime import datetime
import models


class BaseModel:
    """The main class"""
    def __init__(self, *args, **kwargs):
        """Constructor of the instance. Uses kwargs if not empty"""
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def save(self):
        """update time attribute"""
        self.updated_at = datetime.now()

    def __str__(self):
        """return string representation"""
        class_name = "[" + self.__class__.__name__ + "]"
        return class_name + " (" + self.id + ") " + str(self.__dict__)

    def to_dict(self):
        """return dict containing keys/values"""
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = values
       new_dict['__class__'] = self.__class__.__name__

       return new_dict

