#!/usr/bin/python3
""""Creates User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """"Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
