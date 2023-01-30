#!/usr/bin/python3
"""Unittest module to test `base_model`
"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing `BaseModel` instantiation
    """

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_id_is_unique(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_two_models_created_at_different(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertLess(inst1.created_at, inst2.created_at)

    def test_two_models_updated_at_different(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertLess(inst1.updated_at, inst2.updated_at)

    def test_str_method(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "9876543210"
        bm.created_at = bm.updated_at = dt
        str_bm = bm.__str__()
        self.assertIn("[BaseModel] (9876543210)", str_bm)
        self.assertIn("'created_at': " + dt_repr, str_bm)
        self.assertIn("'updated_at': " + dt_repr, str_bm)

    def test_instantiation_with_None_args(self):
        inst = BaseModel(None)
        self.assertNotIn(None, inst.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        inst = BaseModel(id="091", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(inst.id, "091")
        self.assertEqual(inst.created_at, dt)
        self.assertEqual(inst.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        inst = BaseModel(
                "12", id="71425908", created_at=dt_iso,
                updated_at=dt_iso
        )
        self.assertEqual(inst.id, "71425908")
        self.assertEqual(inst.created_at, dt)
        self.assertEqual(inst.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests `save()` method of BaseModel
    """

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

    def test_one_save(self):
        inst = BaseModel()
        first_updated_at = inst.updated_at
        inst.save()
        self.assertLess(first_updated_at, inst.updated_at)

    def test_two_saves(self):
        inst = BaseModel()

        first_updated_at = inst.updated_at
        inst.save()
        second_updated_at = inst.updated_at
        inst.save()
        self.assertLess(first_updated_at, second_updated_at)

    def test_save_with_arg(self):
        inst = BaseModel()
        with self.assertRaises(TypeError):
            inst.save(None)

    def test_save_updates_file(self):
        inst = BaseModel()
        inst.save()
        inst_id = "BaseModel." + inst.id
        with open("file.json", "r") as f:
            self.assertIn(inst_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests `to_dict()` method of a BaseModel Instance."""

    def test_to_dict_type(self):
        inst = BaseModel()
        self.assertTrue(dict, type(inst.to_dict()))

    def test_to_dict_keys(self):
        inst = BaseModel()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())

    def test_to_dict_with_added_attributes(self):
        inst = BaseModel()
        inst.name = "Best School"
        inst.my_number = 89
        self.assertIn("name", inst.to_dict())
        self.assertIn("my_number", inst.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        inst = BaseModel()
        dict_inst = inst.to_dict()
        self.assertEqual(str, type(dict_inst["created_at"]))
        self.assertEqual(str, type(dict_inst["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        inst = BaseModel()
        inst.id = "3814"
        inst.created_at = inst.updated_at = dt
        t_dict = {
            'id': '3814',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(inst.to_dict(), t_dict)

    def test_to_dict_output_to_dict_(self):
        inst = BaseModel()
        self.assertNotEqual(inst.to_dict(), inst.__dict__)

    def test_to_dict_with_arg(self):
        inst = BaseModel()
        with self.assertRaises(TypeError):
            inst.to_dict(None)


if __name__ == "__main__":
    unittest.main()
