import unittest
from employee.emp import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.emp = Employee('John', 'Smith', 80000)

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')

    def test_email_after_name_change(self):
        self.emp.first_name = 'Mike'
        self.assertEqual(self.emp.email, 'mike.smith@mail.com')

    def test_email_after_last_name_change(self):
        self.emp.last_name = 'Moore'
        self.assertEqual(self.emp.email, 'john.moore@mail.com')

    def test_tax(self):
        self.assertEqual(self.emp.tax, 13600)

    def test_tax_2(self):
        self.emp.salary = 100000
        self.assertEqual(self.emp.tax, 17000)

    def test_salary_after_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 880000)
