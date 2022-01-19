import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('abs'.upper(), 'ABS')

    @unittest.skip('Always skipping...')
    def test_case_2(self):
        self.assertEqual('abs'.upper(), 'ABS')


