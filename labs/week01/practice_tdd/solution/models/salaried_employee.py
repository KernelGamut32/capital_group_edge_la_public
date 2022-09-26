from models.employee import Employee


class SalariedEmployee(Employee):
    '''
    Salaried employee
    '''

    def __init__(self, emp_num, f_name, l_name, dept, annual_salary):
        super().__init__(emp_num, f_name, l_name, dept)
        self.annual_salary = annual_salary

    def process_pay(self):
        return self.annual_salary / 52
