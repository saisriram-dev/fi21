class Car:
    # Dunder method is a method that starts and ends with double underscores
    # The main use of __init__ method is to initialize the attributes of the class
    # Called as the constructor method
    def __init__(self, year, model, colour, for_sale): 
        self.year = year # These are called instance variables. 
        self.model = model # They are defined inside the __init__ method
        self.colour = colour # Each object has their own version of these instance variables
        self.for_sale = for_sale

    def describe_car(self):
        print(f"{self.year} {self.colour} {self.model} {self.for_sale}")
