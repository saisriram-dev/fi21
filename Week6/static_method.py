# Static methods

# They are used to create methods that are not bound to a class or instance of a class
# They are used when we don't need object state or class state to perform a task
# They are created using the @staticmethod decorator


class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y


print(Math.add(5, 3))  # Output: 8
print(Math.subtract(5, 3))  # Output: 2


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100


print(Student.is_valid_marks(85))  # True
print(Student.is_valid_marks(150))  # False
