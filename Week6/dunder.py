# Some uselful DUNDER methods


class Student:
    def __init__(self, name, grade, subjects_failed):
        self.name = name
        self.grade = grade
        self.subjects_failed = subjects_failed

    def __repr__(
        self,
    ):  # This is for developers, it should be unambigious and ideally should be able to recreate the object
        return f"Student(name='{self.name}, grade='self.grade', subjects_failed={self.subjects_failed})"

    def __str__(self):  # This is for users, it should be readable and informative
        return f"Hii, I am {self.name}. My grade is {self.grade} and I have failed in {self.subjects_failed} subjects. I will do better next time."

    def __len__(
        self,
    ):  # This is for the length of the object, it should return an integer
        return len(self.subjects_failed)

    def __eq__(self, other):  # This is for equality, it should return a boolean
        return (
            self.grade == other.grade and self.subjects_failed == other.subjects_failed
        )


s1 = Student("Alice", "A", ["Math"])
s2 = Student("Bob", "A", ["Math"])
s3 = Student("Charlie", "B", ["Math", "Science"])

print(
    s1 == s2
)  # This would return False if we had not implemented the __eq__ method, because they are different objects in memory. But since we have implemented it, it will return True because their grades and subjects_failed are the same.
print(s1 == s3)
print(s1)
print(repr(s1))
