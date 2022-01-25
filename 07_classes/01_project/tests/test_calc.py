import unittest
from calculator.calc_math import SimpleMathCalculator

class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.add(4, 5), 9)

    def test_sub(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(4, 5), -1)

    def test_mul(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.mul(4, 5), 20)

    def test_div(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.div(10, 5), 2)

    def test_true_div(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.true_div(15, 5), 3)