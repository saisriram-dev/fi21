# Duck Typing 
# As long as a particular object has a minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# This Car makes sound like an animal, so it can be considered an animal.
# So this a way to achieve polymorphism.
class Car:
    alive = False
    def horn(self):
        print("HONK!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
    print(animal.alive)
