import sys
import unittest

path = r'C:\Users\jacek\PycharmProjects\Python---Unittest\07_classes\02_project'
sys.path.append(path)

from calculator.calculator import SimpleMathCalculator

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