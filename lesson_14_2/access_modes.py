class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self._email = first + '.' + last + '@mail.ru'
        self.pay = pay

emp = Employee('Jon', 'Snow', 32_000)
print(emp.first)
print(emp.last)
print(emp._email)
print(emp.pay)