#class , constructor , destructor

class PartyAnimal:
    beers = 0
    Total_Partyppl = 0
    def __init__(self, z):
        self.name = z
        print(self.name,  'Started the party with ',self.beers ,' Welcome beer')
        PartyAnimal.Total_Partyppl += 1

    #method/function of the class Party Animal
    def party(self):
        self.beers = self.beers + 1
        print(self.name, 'party continues with', self.beers,)

class Rav(PartyAnimal):
    beers = 1
    def drink(self):
        self.beers = self.beers + 1
        print(self.name, 'drank ', self.beers, 'beers')

#instantiation of this class to an object a
r = Rav("Rani")
r.party()
r.drink()

p = PartyAnimal('Pappu')
print('total ppl on party', PartyAnimal.Total_Partyppl)
print(help(Rav))
