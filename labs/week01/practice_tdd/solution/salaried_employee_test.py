import unittest
from models.salaried_employee import SalariedEmployee


class TestSalariedEmployee(unittest.TestCase):
    def setUp(self):
        self.salaried_employee = SalariedEmployee(emp_num='DEF456', f_name='Bob',
                            l_name='Roberts', dept='HR', annual_salary=50000)

    def test_exists(self):
        self.assertIsNotNone(self.salaried_employee)

    def test_print_badge(self):
        badge_text = self.salaried_employee.print_badge()
        self.assertEqual(
            f'Employee Number: {self.salaried_employee.emp_num}\nName: {self.salaried_employee.l_name}, {self.salaried_employee.f_name}\nDepartment: {self.salaried_employee.dept}',
            badge_text)
    
    def test_process_pay(self):
        pay_amt = self.salaried_employee.process_pay()
        self.assertEqual(50000 / 52, pay_amt)
