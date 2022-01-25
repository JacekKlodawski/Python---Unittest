import unittest
from calculator.calc_math import SimpleMathCalculator

def setUpModule():
    print('Setting up module')
    global calc
    calc = SimpleMathCalculator()

def tearDownModule():
    print('Tearing down')
    global calc
    del calc

class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(4, 5), 9)

    def test_sub(self):
        self.assertEqual(calc.sub(4, 5), -1)

    def test_mul(self):
        self.assertEqual(calc.mul(4, 5), 20)