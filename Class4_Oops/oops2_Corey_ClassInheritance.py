#class , constructor , destructor
class Emp:
    Total_Emp = 0
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

######## Inherit a class from the main class ###############
class Developer(Emp):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lng = prog_lang

class Manager(Emp):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.emp = []
        else:
            self.emp = employees

    def add_emp(self, Emp_Name):
        if Emp_Name not in self.emp:
            self.emp.append(Emp_Name)

    def remove_emp(self, Emp_Name):
        if Emp_Name in self.emp:
            self.emp.remove(Emp_Name)

    def print_emp(self):
        for i in self.emp:
            print('---> ', Emp.fullname(i))

#emp1 = Emp('Mars', 'Planet', 50000)
#emp2 = Emp('Earth', 'Home', 70000)

dev1_str = 'Mars-Planet-50000'
dev2_str = 'Earth-Home-70000'
dev3 = Emp('Deepak', 'Varma', 60000)

dev1 = Emp.fromstring(dev1_str)
dev2 = Emp.fromstring(dev2_str)
print('With Defaults : ',dev1.__dict__)
mgr_1 = Manager('John', 'Smith', 90000)

mgr_1.add_emp(dev1)
mgr_1.add_emp(dev2)
mgr_1.add_emp(dev3)
mgr_1.print_emp()

mgr_1.remove_emp(dev1)
mgr_1.print_emp()

print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Emp))
