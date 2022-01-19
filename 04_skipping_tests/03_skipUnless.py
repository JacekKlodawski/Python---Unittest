import unittest
import sys

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('abs'.upper(), 'ABS')

    @unittest.skipUnless(sys.platform.strtswith('win'),'Requires Windows.')
    def test_case_2(self):
        self.assertEqual('abs'.upper(), 'ABS')

    @unittest.skipUnless(sys.platform.strtswith('linux'), 'Requires Linux.')
    def test_case_3(self):
        self.assertEqual('abs'.upper(), 'ABS')