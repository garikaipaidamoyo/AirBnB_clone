#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py


Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""


import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage instantiation(unittest.TestCase):
    """ Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_str(self):
        self.assertEqual(dict, type(FileStorage.__FileStorage__objects))

    def test_file_storage_initializes(self):
        self.assertEqual(type(models.file_storage), Filestorage)


class TestFileStorage_methods(unittest.TestCase):

    """Unittests for testing methods pf the FileStorage class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage.__FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.file_storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.file_storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.file_storage.new(bm)
        models.file_storage.new(us)
        models.file_storage.new(st)
        models.file_storage.new(pl)
        models.file_storage.new(cy)
        models.file_storage.new(am)
        models.file_storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.file_storage.all().keys())
        self.assertIn(bm, models.file_storage.all().values())
        self.assertIn("User." + us.id, models.file_storage.all().keys())
        self.assertIn(us, models.file_storage.all().values())
        self.assertIn("State." + st.id, models.file_storage.all().keys())
        self.assertIn(st, models.file_storage.all().values())
        self.assertIn("Place." + pl.id, models.file_storage.all().keys())
        self.assertIn(pl, models.file_storage.all().values())
        self.assertIn("City." + cy.id, models.file_storage.all().keys())
        self.assertIn(cy, models.file_storage.all().values())
        self.assertIn("Amenity." + am.id, models.file_storage.all().keys())
        self.assertIn(am, models.file_storage.all().values())
        self.assertIn("Review." + rv.id, models.file_storage.all().keys())
        self.assertIn(rv, models.file_storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.file_storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.file_storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.file_storage.new(bm)
        models.file_storage.new(us)
        models.file_storage.new(st)
        models.file_storage.new(pl)
        models.file_storage.new(cy)
        models.file_storage.new(am)
        models.file_storage.new(rv)
        models.file_storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.file_storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.file_storage.new(bm)
        models.file_storage.new(us)
        models.file_storage.new(st)
        models.file_storage.new(pl)
        models.file_storage.new(cy)
        models.file_storage.new(am)
        models.file_storage.new(rv)
        models.file_storage.reload()
        objs = FileStorage.__FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.file_storage.reload(None)


if __name__ == "__main__":
    unittest.main()
