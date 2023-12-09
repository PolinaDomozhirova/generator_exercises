import unittest
from src.employee import Employee

class EmployeeBaseTest(unittest.TestCase):

    def test_create_employee_ideal(self):
        instance = Employee('2', '2', 20)
        self.assertEqual(instance.name, '1')
        self.assertEqual(instance.surname, '2')
        self.assertEqual(instance.age, 20)