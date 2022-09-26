class Employee():
    def __init__(self, emp_num, f_name, l_name, dept):
        self.emp_num = emp_num
        self.f_name = f_name
        self.l_name = l_name
        self.dept = dept

    def print_badge(self):
        return 'Employee Number: {}\nName: {}, {}\nDepartment: {}'.format(self.emp_num, self.l_name, self.f_name, self.dept)
