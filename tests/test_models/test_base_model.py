#!/usr/bin/env python3
"""
Unittest for ```base_model```
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test the class ``BaseModel`` """

    def setUp(self):
        self.model1 = BaseModel()
        test_args = {'created_at': datetime(2017, 2, 10, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 10, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_class_doc(self):
        """ Test ``BaseModel`` class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docs(self):
        """ Test methods in ``BaseModel`` for documentation"""
        methods = [
            BaseModel.__init__, BaseModel.__str__,
            BaseModel.save, BaseModel.to_dict
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_initial_attribute(self):
        """ Test object id"""
        test_model = BaseModel()
        test_model2 = BaseModel()

        # check if id exists, not NULL and a string
        self.assertTrue(hasattr(test_model, 'id'))
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.id, str)

        # Check if id is uuid
        self.assertTrue(uuid.UUID(test_model.id))

        # Check if two instances have the same id
        self.assertNotEqual(test_model.id, test_model2.id)

        # Check if created_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'created_at'))
        self.assertIsNotNone(test_model.created_at)
        self.assertIsInstance(test_model.created_at, datetime)

        # Check if updated_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'updated_at'))
        self.assertIsNotNone(test_model.updated_at)
        self.assertIsInstance(test_model.updated_at, datetime)

        # Check if updated_at time is after created_at
        self.assertGreater(test_model.updated_at, test_model.created_at)

        # Check that *args was not used
        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)

        # Check if __str__ prints correct output
        str_ = "[BaseModel] ({}) {}".format(test_model.id, test_model.__dict__)
        self.assertEqual(str(test_model), str_)

    def test_kwargs_input(self):
        """ Test ``BaseModel`` initialization with kwargs"""
        dic = {
            'id': 'test_id',
            'created_at': '2023-08-09T12:34:56.789012',
            'updated_at': '2023-08-09T13:45:12.345678',
            'name': 'Wills',
            'value': 42
        }
        test_model = BaseModel(**dic)

        self.assertEqual(test_model.id, "test_id")
        self.assertEqual(test_model.name, "Wills")
        self.assertEqual(test_model.value, 42)
        self.assertIsInstance(test_model.created_at, datetime)
        self.assertIsInstance(test_model.updated_at, datetime)

    def test_to_dict_data_type(self):
        """ Test each data type after ``to_dict`` """
        test_model = BaseModel()
        test_model.name = "Sabah"
        test_model.age = "lol"
        test_model.num = 12
        test_model.float_num = 12.21
        test_model.bool_val = True

        test_dict = test_model.to_dict()

        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(test_dict["id"], test_model.id)
        self.assertEqual(test_dict["name"], "Sabah")
        self.assertEqual(test_dict["age"], "lol")
        self.assertEqual(test_dict["num"], 12)
        self.assertEqual(test_dict["float_num"], 12.21)
        self.assertEqual(test_dict["bool_val"], True)

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)

    def test_save(self):
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)


if __name__ == "__main__":
    unittest.main()
