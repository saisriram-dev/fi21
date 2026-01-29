# Multiple Inheritance = inheriting from more than one parent class
#                       C(A, B)

# Multi-level Inheritance = inheriting from a parent class that inherits from another parent class
#                       C(B(A)), Parent class A -> Parent class B(A) -> Child class C

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

# Prey and Predator classes inherit from the Animal class
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

# Rabbit, Hawk and Fish classes inherit from the Prey and Predator classes
# As Prey and Predator classes also inherit from the Animal class the Rabbit, Hawk and Fish classes also inherit from the Animal class
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# This is know as multiple inheritance
# Multiple inheritance allows a class to inherit from multiple parent classes
class Fish(Prey, Predator): # They hunt smaller fish and fall prey to bigger fish, hawks and other animals etc.
    pass

rabbit = Rabbit("Bugs Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")
""" This is known as multi-level inheritance
    Multi-level inheritance allows a class to inherit from a parent class that inherits from another parent class.
    So the class has access to all the attributes and methods of the parent class and the parent class of the parent class.
    In this case, the Fish class inherits from the Prey and Predator classes, which inherits from the Animal class.
    So the fish class has access to all the attributes and methods of the Prey, Predator classes and inturn has access to 
    all the methods of the Animal class as it is the parent class of the Prey and Predator classes."""
