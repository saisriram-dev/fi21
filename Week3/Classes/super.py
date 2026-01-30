# super() = Function used in a child class to call methods from a parent class(superclass).
#           Allows you to access methods from a parent class without having to create an object of the parent class.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    # As we are using another constructor it will override the parent's constructor i.e, we won't be able to access the parent's attributes
    # So we have to recreate the filled and radius attributes using self.filled = filled etc.,
    # So we need to re-write code. So, instead of it we could use super().__init__(color, filled) to get the parent's constructor and use it's attributes
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    # If a child shares a similar method with the parent class, it will use the child's method
    # So we are using a super method to call the similar method from the parent class
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of { 3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of { 3.14 * self.width * self.width}")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of { 0.5 * self.width * self.height}")
