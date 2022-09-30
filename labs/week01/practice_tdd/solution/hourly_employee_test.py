import unittest
from models.hourly_employee import HourlyEmployee


class TestHourlyEmployee(unittest.TestCase):
    def setUp(self):
        self.hourly_employee = HourlyEmployee(emp_num='DEF456', f_name='Bob',
                            l_name='Roberts', dept='HR', hourly_rate=15.00)

    def test_exists(self):
        self.assertIsNotNone(self.hourly_employee)

    def test_print_badge(self):
        badge_text = self.hourly_employee.print_badge()
        self.assertEqual(
            f'Employee Number: {self.hourly_employee.emp_num}\nName: {self.hourly_employee.l_name}, {self.hourly_employee.f_name}\nDepartment: {self.hourly_employee.dept}',
            badge_text)
    
    def test_process_pay(self):
        pay_amt = self.hourly_employee.process_pay()
        self.assertEqual(600, pay_amt)

if __name__ == "__main__":
    unittest.main()