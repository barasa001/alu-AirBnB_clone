#!/bin/usr/python3
"""defines base model class"""
import uuid
from datetime import datetime
import models


class models:
    """Base model class"""
    def __init(self, args, **kwargs):
        """initiate class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key !="__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        def __str__(self):
            """return string representaion of the class"""
            return "[{}] ({}) {}".format(self.__class__.__name

         def save(self):
        """ update of attribute updated_at with latest time
        updated_at: datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        get the objects of the instance
        returns: dictionary
        """
        temp_dict = dict(self.__dict__)
        temp_dict['__class__'] = __class__.__name__
        temp_dict['created_at'] = temp_dict['created_at'].isoformat()
        temp_dict['updated_at'] = temp_dict['updated_at'].isoformat()
        return temp_dict

