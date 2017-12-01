
class Pet(object):

    # initializing class
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


francisca = Pet("Francisca", "Mongrel dog")
print (francisca)
print ("The dog's name is %s" % (francisca.getName()))

polly = Pet("Polly", "parrot")
print(polly)

# if not running here
# from Pet_Class import Pet
# francisca = Pet("Francisca", "Mongrel dog")
# print ("The dog's name is %s" % (francisca.getName()))
# print ("The dog's name is %s" % (Pet.getName(francisca)))

## Creating subclasses

class Dog(Pet):

    def __init__ (self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


class Cat(Pet):

    def __init__ (self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

class Bird(Pet):

    def __init__ (self, name, hates_cats):
        Pet.__init__(self, name, "Bird")
        self.hates_cats = hates_cats

    def hatesDogs(self):
        return self.hates_cats

littleDog = Dog ("Cute", True)
charlie = Cat ("Charlie", False)

print (isinstance(littleDog, Dog))

print (isinstance(littleDog, Cat))

print (isinstance(francisca, Dog))

print (isinstance(francisca, Pet))

print ("%s chases cats: %s " % (littleDog.getName(), littleDog.chasesCats()))

print ("%s hates dogs: %s " % (charlie.getName(), charlie.hatesDogs()))