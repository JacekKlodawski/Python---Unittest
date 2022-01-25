import unittest
from calculator.calc_math import SimpleMathCalculator

class TestSimpleMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class.')
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('tearing down class.')
        del cls.calc

    def test_add_int(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_add_float(self):
        self.assertAlmostEqual(self.calc.add(4.6, 5.5), 10.1)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-4, -5), -9)

class TestSimpleMathCalculatorSubtract(unittest.TestCase):

    def test_sub_int(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(4, 5), -1)

    def test_sub_float(self):
        calc = SimpleMathCalculator()
        self.assertAlmostEqual(calc.sub(4.9, 5.7), -0.8)
