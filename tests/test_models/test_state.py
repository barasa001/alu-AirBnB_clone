#!/usr/bin/python3
"""unittest for testing states"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestCaseState(unittest.TestCase):

    def test_instance(self):
        """ test instance type """
        state = State()
        self.assertIsInstance(state, State)

    def test_is_class(self):
        """ test class """
        state = State()
        self.assertEqual(str(type(state)),
                         "<class 'models.state.State'>")

    def test_is_subclass(self):
        """ test is subclass """
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_state_name(self):
        """ test state name """
        state = State()
        state.name = ""
        self.assertEqual(state.name, '')
        self.assertIsNotNone(state.id)

    if __name__ == "__main__":
        unittest.main()

