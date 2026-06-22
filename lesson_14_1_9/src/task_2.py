import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @classmethod
    def set_raise_amt(cls, new_rise_amt):
        cls.raise_amt = new_rise_amt


# emp_1 = Employee('Jon', 'Snow', 50000)
# emp_2 = Employee('Ivan', 'Ivanov', 60000)
# print(Employee.raise_amt)
#
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
#
# emp_str_1 = 'Jon-Snow-70000'
# emp_str_2 = 'Ivan-Ivanov-30000'
# emp_str_3 = 'Elena-Nikitina-90000'
#
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)


# my_date = datetime.date(2023, 1, 31)
# print(Employee.is_workday(my_date))