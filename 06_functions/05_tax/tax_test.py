import unittest
from tax import calc_tax

class TestTax(unittest.TestCase):

    def test_age_is_positive(self):
        self.assertRaises(ValueError, calc_tax, 100, 0.1, -5)

    def test_age_is_integer(self):
        self.assertRaises(TypeError, calc_tax, 100, 0.1, 5.5)

    def test_age_is_under_18_less_than_5k(self):
        self.assertEqual(calc_tax(100, 0.1, 7), 10)

    def test_age_is_under_18_more_than_5k(self):
        self.assertEqual(calc_tax(60000, 0.1, 7), 5000)

    def test_age_is_under_65(self):
        self.assertEqual(calc_tax(100, 0.1, 45), 10)

    def test_age_is_over_65_more_than_8k(self):
        self.assertEqual(calc_tax(90000, 0.1, 76), 8000)

    def test_age_is_over_65_less_than_8k(self):
        self.assertEqual(calc_tax(1000, 0.1, 76), 100)

