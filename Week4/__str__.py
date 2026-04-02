# Demonstartion of the usage if the __str__ method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """When we create an object using a selected class, whenever we try to print that object
    it will print the memory address of that object. To avoid this, we can use the __str__ method
    to return a string representation of the object. So now after an object is created if we were 
    to print that object, it executes the __str__ method and returns the string representation of that object 
    instead of the memory address."""

    def __str__(self):
        return f"{self.name} is {self.age} years old."


person1 = Person("Alice", 30)
# If we were to print the person1 object without the __str__ method, it would print the memory address of that object.
# But with the __str__ method, it will print the string representation of that object.
# Output: Alice is 30 years old.
print(person1)
