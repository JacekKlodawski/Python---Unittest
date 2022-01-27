import unittest
from parameterized import parameterized
from calculator.calc import SimpleMathCalculator

class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    @parameterized.expand([
        (-3, -2, -5),
        (-3, 2, -1),
        (3, -2, 1),
        (3, 2, 5)
    ])
    def test_add(self, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)