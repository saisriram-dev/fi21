# Inheritance
# Inheritance is a way to create a new class from an existing class.
# It helps with code reusability and modularity.
# class ChildClass(ParentClass):
class Animal:
    def __init__(self, name, is_alive = True):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# The below classes inherit from the Animal class
# They can access the attributes and methods of the parent class "Animal"
class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Mouse(Animal):
    def sound(self):
        print("Squeak")

# Creating objects of the child classes
dog = Dog("Scooby")
cat = Cat("Whiskers")
mouse = Mouse("Mickey")

# These methods are inherited from the parent class "Animal"
print(dog.name)
dog.eat()

# These methods are specific to the child classes
dog.sound()
cat.sound()
mouse.sound()
