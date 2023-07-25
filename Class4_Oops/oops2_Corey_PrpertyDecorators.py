#class , constructor , destructor
class Emp:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
#1        self.email  = first + '.' + last + '@company.com'

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.email)

    @property #2 - adding property will allow us to set the attribute directly, dont need to call the method just access it as attribute
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    @property #2
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    ###### 5 now adding a setter function which can handle problem with fullname method
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #6 - a deleter
    @fullname.deleter
    def fullname(self):
        print('Deleting the', self)
        self.first = None
        self.last = None


emp1 = Emp('Mars', 'Planet', 50000)
emp2 = Emp('Earth', 'Home', 70000)
emp3 = Emp('Deepak', 'Varma', 60000)

#print('With Defaults : ',emp1.__dict__)
#emp1.apply_raise()

#3 if you want to access the property fullname, just to change the first and last name
emp1.fullname = 'Deepak Varma'
#emp1.first = 'Venus'
print(emp1.first)
print(emp1.email)
print(emp1.fullname) #3 it throw error AttributeError: can't set attribute, why cause some changes needed in fullname property
#2 print(emp1.fullname())
#1 print(emp1.email)
#2 print(emp1.email())

del emp1.fullname

#print(emp1.__dict__)