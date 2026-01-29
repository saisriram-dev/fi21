# Abstract classes
# We can't create objects from abstract classes
# We can only create child classes from abstract classes
# All the methods in the abstract class should be implmented in the child class
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    # We can't define what a method should be or does in an abstract class
    # We can only define that the method should be implemented in the child class
    # What the method does, should be defined in the child class
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
# car = Vehicle(). This will throw an error because we can't create objects from abstract classes

# All methods in the abstract classes should be implemented in the child classes otherwise we will get an error
class Motorcycle(Vehicle):
    def go(self):
        print("I'm a motorcycle, I'm going!")

    def stop(self):
        print("I'm a motorcycle, I'm stopping!")

class Car(Vehicle):
    def go(self):
            print("I'm a car, I'm going!")

    def stop(self):
            print("I'm a car, I'm stopping!")
