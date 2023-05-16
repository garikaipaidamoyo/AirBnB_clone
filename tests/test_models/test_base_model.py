#!/usr/bin/python3

from models import base_model
from models.base_model import BaseModel

mod = BaseModel()
mod.name = "My First Model"
mod.my_number = 89
print(mod)
mod.save()
print(mod)
mod_json = mod.to_dict()
print(mod_json)
print("JSOM of my_model:")
for key in mod_json.keys():
    print("\t{}: ({}) - {}".format(key, type(mod_json[key]), mod_json[key]))
