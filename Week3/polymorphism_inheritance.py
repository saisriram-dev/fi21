# Polymorphism = greek word for many forms or faces, Poly = many, morph = form, Polymorph = many forms

# There are 2 ways to achieve polymorphism
# 1. Inheritance
# 2. Duck typing
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

# Pizza inherits feom Circle so it can use the area method.
# Also Circle inherits from Shape so it can use the area method
# Also now Pizza has three forms; 1. A Pizza, 2. A Circle and 3. A Shape
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

# Our circle, square and triangle objects are all inherit from the shape class and are all shapes(2 forms)
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm²")
