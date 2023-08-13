#!/usr/bin/env python3
"""
Unittest for ```User``` class
"""
import unittest
from models.user import User


class UserTest(unittest.TestCase):
    '''class for User tests'''

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.password, "")


if __name__ == '__main__':
    unittest.main()
