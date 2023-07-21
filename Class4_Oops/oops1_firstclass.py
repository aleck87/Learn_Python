#class , constructor , destructor

class PartyAnimal:
    x = 0

###### about the self - it a default placeholder you named as argument to method
    #constructor
    def __init__(self):
        print('I am constructed ')

    #method/function of the class Party Animal
    def party(self):
        self.x = self.x + 1
        print('So far :', self.x)

    #destructor
    def __del__(self):
        print('I am destructed ')

#instantiation
an = PartyAnimal()

#calling methods

an.party()
an.party()

#if you de-reference the object or program ends then the class calls the destructor that this object doesnt belong to class anymore
an = 42
