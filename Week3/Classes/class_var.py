class Students:
    # The below are class variables
    # They are defined outside the __init__ method
    # They can be accessed by all instances or objects of the class
    year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_students += 1

student1 = Students("John", 16)
student2 = Students("Jane", 17)

print(f"Year: {Students.year}")
print(f"Number of students: {Students.num_students}")
print(f"Student 1 name: {student1.name}, age: {student1.age}")
print(f"Student 2 name: {student2.name}, age: {student2.age}")
