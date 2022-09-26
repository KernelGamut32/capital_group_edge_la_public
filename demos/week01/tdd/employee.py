class Employee():
    '''
    Describes simple employee class
    '''
    def __init__(self, salary):
        self.salary = salary

    def give_raise(self, amt=5000):
        self.salary += amt