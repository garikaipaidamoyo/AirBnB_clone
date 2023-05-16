#!/usr/bin/python3
""" Defines tests for models/amenity.py

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """ Unittest for testing instantiation of the Amenity class"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_obj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_class_attrb(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_unused_agr(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_kwagrs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """ Unittests for testing save method of the Amenity class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOErrror:
            pass

    def test_one_saved(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_save_args(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

        def test_save_updates(self):
            am = Amenity()
            am.save()
            am_id = "Amenity" + am.id
            with open("file.json", "r") as f:
                self.assertIn(am_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """ Tests for to_dict method of the Amenity class"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        _dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), _dict)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
