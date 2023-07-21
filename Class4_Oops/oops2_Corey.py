#class , constructor , destructor

class Emp:
    Total_Emp = 0
    Raise     = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'

        Emp.Total_Emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.Raise)

emp1 = Emp('Mars', 'Planet', 50000)
emp2 = Emp('Earth', 'Home', 70000)

print(emp1.__dict__)
emp1.apply_raise()

print(emp1.__dict__)