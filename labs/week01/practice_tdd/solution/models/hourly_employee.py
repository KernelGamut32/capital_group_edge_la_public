from models.employee import Employee


class HourlyEmployee(Employee):
    '''
    Hourly employee
    '''

    def __init__(self, emp_num, f_name, l_name, dept, hourly_rate):
        super().__init__(emp_num, f_name, l_name, dept)
        self.hourly_rate = hourly_rate

    def process_pay(self):
        return self.hourly_rate * 40
