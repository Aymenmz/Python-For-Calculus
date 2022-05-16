class Employee:
    number_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.number_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


print(Employee.number_emps)

emp_1 = Employee('AYMEN', 'MAIZIZ', 10000)
emp_2 = Employee('RIO', 'MAIZIZ', 20000)

print(Employee.number_emps)

print(emp_1.fullname())
print(emp_2.fullname())
