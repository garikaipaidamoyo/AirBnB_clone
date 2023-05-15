#!/usr/bin/python3
"""Define unittests for city class in model/city.py


Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class"""

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="364", created_at=dt_iso, updates_at=dt_iso)
        self.assertEqual(cy.id, "364")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.update_at, dt)

    def test_instantiation_no_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_no_args_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_two_cities_unique_uid(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_unused_args(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_string_represtantion(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cy_str = cy.__str__()
        self.assertIn("[City] (123456)", cy_str)
        self.assertIn("'id': '123456'", cy_str)
        self.assertIn("'created_at': " + dt_repr, cy_str)
        self.assertIn("'updated_at': " + dt_repr, cy_str)


class TestCitySave(unittest.TestCase):
    """Tests for the save method of the City class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        excpet IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        excpet IOError:
            pass

    def test_save_one(self):
        cy = City()
        sleep(0.05)
        first_update = cy.updated_at
        cy.save()
        self.assertLess(first_update, cy.updated_at)

    def test_arg_saved(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_updates_saved(self):
        cy = City()
        cy.save()
        cy_id = "City" + cy.id
        with open("file.json", "r") as fp:
            self.assertIn(cy_id, f.read())


class TestCity_dict(unittest.TestCase):
    """ testing for to_dictionary method in City class"""

    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_At = cy.updated_at = dt
        _dict = {
            'id': '123456',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'City',
        }
        self.assertDictEqual(cy.to_dict(), _dict)

    def test_to_dict_with_args(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
