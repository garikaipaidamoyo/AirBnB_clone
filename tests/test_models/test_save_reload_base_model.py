#!/usr/bin/python3

from models.engine import file_storage
from models.base_model import BaseModel

all_objs = file_storage.all()
print("--Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
MyModel = BaseModel()
MyModel.name = "My_First_Model"
MyModel.my_number = 89
MyModel.save()
print(MyModel)
