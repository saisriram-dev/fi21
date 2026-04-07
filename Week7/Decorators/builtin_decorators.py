class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property  # This is a built-in decorator that allows us to access the method as an attribute
    def area(self):
        return 3.14 * self.radius**2


Circle1 = Circle(5)
print(
    Circle1.area
)  # No need to call the method with parentheses, we can access it like an attribute


# A method that receives the class itself (cls) as its first argument instead of an instance (self).
# It can be called on the class directly, without creating an object.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_string(cls, name_string):  # alternative constructor
        name = name_string.strip().title()
        return cls(name)  # creates a new Dog instance


Dog.get_species()  # 'Canis familiaris'
d = Dog.from_string("  buddy  ")  # Dog(name='Buddy')


# A method that belongs to the class logically, but receives neither self nor cls.
# It's just a plain function namespaced inside the class.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


MathUtils.add(3, 4)  # 7
MathUtils.is_even(10)  # True
