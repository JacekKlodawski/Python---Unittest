import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance('abs', str))

    def test_case_2(self):
        self.assertTrue(isinstance('abs', int))

    def test_case_3(self):
        self.assertFalse(isinstance('abs', str))

    def test_case_4(self):
        self.assertFalse(isinstance('abs', int))