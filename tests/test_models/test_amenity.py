#!/usr/bin/env python3
"""
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''class for TestAmenity'''
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
