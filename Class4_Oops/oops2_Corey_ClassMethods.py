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
######### Regular Methods - are the once which takes an instance/object as argument and works on that
################# No need of decorator
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int (self.pay * self.Raise)

    #### class methods are the once which takes an class as argument and used to access the class variable and to make an alternative constructor
    @classmethod # decorator
    #cls is a way similar to self: to access the class variables
    def raise_amount(cls, amount):
        cls.Raise = float(amount)

    @classmethod
    def fromstring(cls, emp_str):
        first, last, pay = emp_str.split('-')
        pay = int(pay)
        return Emp(first, last, pay)

#### static methods are the once which doesnt takes an class or object or instance as argument but are logically belongs to a class
#  and performs a set of operations independent of class, object and so
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#emp1 = Emp('Mars', 'Planet', 50000)
#emp2 = Emp('Earth', 'Home', 70000)

emp1_str = 'Mars-Planet-50000'
emp2_str = 'Earth-Home-70000'
emp3 = Emp('Deepak', 'Varma', 60000)

emp1 = Emp.fromstring(emp1_str)
emp2 = Emp.fromstring(emp2_str)
print('With Defaults : ',emp1.__dict__)
#emp1.apply_raise()

# with class method
Emp.raise_amount(1.05)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.__dict__)
print(emp3.__dict__)

import datetime

mydate = datetime.date(2023, 5, 6)
print(Emp.is_workday(mydate))

print(dir(datetime))