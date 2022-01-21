import unittest
from tax import calc_tax

class TestTax(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(calc_tax(100, 0.1), 10)

    def test_case_2(self):
        self.assertEqual(calc_tax(100, 0.14), 14)

    def test_case_3(self):
        self.assertRaises(TypeError, calc_tax, 'bo', 0.23)

    def test_case_4(self):
        self.assertRaises(ValueError, calc_tax, -15, 0.23)
