import unittest
from models.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(emp_num='ABC123', f_name='Melissa',
                            l_name='Testing', dept='Accounting')
        
    def test_exists(self):
        self.assertIsNotNone(self.employee)

    def test_print_badge(self):
        badge_text = self.employee.print_badge()
        self.assertEqual(
            f'Employee Number: {self.employee.emp_num}\nName: {self.employee.l_name}, {self.employee.f_name}\nDepartment: {self.employee.dept}',
            badge_text)
