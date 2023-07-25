# __repr__ -  The goad of this method is to be unambiguous

# __str__ - The goal of this method is to be readable

import datetime
#class , constructor , destructor, repr, str
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
########### Dunder/Magic Methods : repr and str ! ####################
# repr and str runs automatically when an object of class is addressed like constructors or des

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.email)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

#emp1 = Emp('Mars', 'Planet', 50000)
#emp2 = Emp('Earth', 'Home', 70000)

emp1_str = 'Mars-Planet-50000'
emp2_str = 'Earth-Home-70000'
emp3 = Emp('Deepak', 'Varma', 60000)

emp1 = Emp.fromstring(emp1_str)
emp2 = Emp.fromstring(emp2_str)
print('With Defaults : ',emp1.__dict__)

## calling the print emp1 directly calls the __str__ method if available otherwise __repr__
print(emp1)

#### we can call them separately as well with the object
print(emp1.__repr__())
print(emp1.__str__())

print(1 + 2)
print(int.__add__(1,2))

#### Object overloading: when an
print(emp1 + emp2)