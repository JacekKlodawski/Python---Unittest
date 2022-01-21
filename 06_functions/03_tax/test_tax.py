import unittest
from tax import calc_tax

class TestTax(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(calc_tax(100, 10), 10)

    def test_case_2(self):
        self.assertEqual(calc_tax(100, 14), 14)

    def test_case_3(self):
        self.assertAlmostEqual(calc_tax(100, 14), 14)

