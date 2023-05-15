#!/usr/bin/python3
""" Module for storage class"""

import datetime
import json
import os


class FileStorage:
    """ Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return file_storage.__objects

    def new(self, obj):
        """Sets __objects in the obj eith key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        file_storage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to json file"""
        with open(file_storage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in file_storage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their reference"""
        from models.base_model import Basemodel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ Reloads the stored objects"""
        if not os.path.isfile(file_storage.__file_path):
            return
        with open(file_storage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            file_storage.__objects.update(obj_dict)
            file_storage.__objects = obj_dict

    def attributes(self):
        """Returns the attributes for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first:name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
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
        return attributes
