class Employee:
    company = "TCS"

    def __init__(self, name):
        self.name = name

    # This is a class method, it can be called on the class itself, it takes the class as the first argument
    # It is used to change the class variable, it can also be used as an alternative constructor
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # TCS
print(e2.company)  # TCS

# Even though we are calling the change_company method on the instance e1,
# it is actually changing the class variable company for all instances of the class Employee,
# because it is a class method and it takes the class as the first argument.
e1.change_company("Google")

print(e1.company)  # Google
print(e2.company)  # Google
