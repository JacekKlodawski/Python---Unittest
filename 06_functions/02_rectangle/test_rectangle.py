import unittest
from rectangle import area, peri

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, "4", 5)
        self.assertRaises(TypeError, area, 4, "5")

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)

class TestPerimeter(unittest.TestCase):

    def test_peri(self):
        self.assertEqual(peri(4, 5), 18)

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, peri, "4", 5)
        self.assertRaises(TypeError, peri, 4, "5")

    def test_perimeter_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, peri, -4, 5)
        self.assertRaises(ValueError, peri, 4, -5)