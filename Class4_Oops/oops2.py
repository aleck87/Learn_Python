#class , constructor , destructor

class PartyAnimal:
    x = 0
    num = 0
    def __init__(self, z):
        self.name = z
        print(self.name,  'constructed ')
        PartyAnimal.num += 1

    #method/function of the class Party Animal
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count :', self.x)

#instantiation of this class to an object a
a = PartyAnimal('Ants')
a.x = 10 # I have assigned the value to a class var belongs to object a
a.party()

# another object
b = PartyAnimal('bali')
b.party()

# lets changes the class variable itself
PartyAnimal.x = 5

# and now print the different x values belongs to objects a and b
a.party()
b.party()

# just change the x for object b
b.x=5
b.party()

c = PartyAnimal('Coley')
PartyAnimal.party(c)
print('Number of ppl in party', PartyAnimal.num)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(PartyAnimal.__dict__)