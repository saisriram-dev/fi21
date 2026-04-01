# Sometimes we don't get data in the way we want in real life.
# So, for these type of cases we can use alternate constructors.
# We basically use class methods to create alternate constructors.
# Ans the class method uses __init_ method to create the object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age = age
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split("-")
        return cls(name, int(age)) # This internally calls __init__
    
student1 = Student("John", 20)
student2 = Student.from_string("Jane-22")
print(student1.name, student1.age) # Output: John 20
print(student2.name, student2.age) # Output: Jane 22
