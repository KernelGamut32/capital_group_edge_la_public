import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    '''
    Tests for simple employee class
    '''

    def setUp(self) -> None:
        self.employee = Employee(salary=50000)

    def test_exists(self):
        self.assertIsNotNone(self.employee)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(55000, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(amt=10000)
        self.assertEqual(60000, self.employee.salary)


if __name__ == 'main':
    unittest.main()
