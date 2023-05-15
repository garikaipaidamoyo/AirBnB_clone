#!/usr/bin/python3
"""Airbnb project base model"""

import uuid
from datetime import datetime
from models.engine import file_storage

class BaseModel:
    """ Class that defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of non-keyworded arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.striptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.striptime(
                        kwargs["updated_at"], "%Y-%m-%dT&H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            file_storage.new(self)

    def __str__(self):
        """ Returns official string format """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        file_storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
