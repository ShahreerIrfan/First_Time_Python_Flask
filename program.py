# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} makes a sound."

# Derived class Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return f"{self.name}, the {self.breed}, barks."

# Derived class Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return f"{self.name}, the {self.breed}, meows."

# Function to describe the animal
def describe_animal(animal):
    print(f"This is {animal.name}, a {animal.species}.")
    print(animal.make_sound())

# Creating objects of Dog and Cat classes
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", breed="Siamese")

# Describing the animals
describe_animal(dog)
describe_animal(cat)
# .........

# Adding another Animal for variety
generic_animal = Animal(name="Shadow", species="Horse")
describe_animal(generic_animal)
