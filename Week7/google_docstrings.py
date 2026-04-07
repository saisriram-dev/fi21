"""
This module demonstrates the use of Google-style docstrings in Python functions and classes.
Each function and method includes a docstring that describes its purpose, arguments, and return values.

Format:
    Brief description of the function or class.

    Args:
        arg1 (type): Description of arg1.
        arg2 (type): Description of arg2.

    Returns:
        type: Description of the return value.
"""

from typing import Any


def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of the two numbers.
    """
    return a + b


def calculate_average(nums: list[int]) -> float:
    """Calculate the average of a list of integers.

    Args:
        nums (list[int]): List of numbers.

    Returns:
        float: Average value.
    """
    return sum(nums) / len(nums)


def count_words(text: str) -> dict[str, int]:
    """Count frequency of each word in a string.

    Args:
        text (str): Input sentence.

    Returns:
        dict[str, int]: Word frequency dictionary.
    """
    words = text.split()
    freq: dict[str, int] = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def find_user(user_id: int) -> str | None:
    """Find a user by ID.

    Args:
        user_id (int): User ID.

    Returns:
        str | None: Username if found, otherwise None.
    """
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


class Student:
    """Represents a student with marks."""

    def __init__(self, name: str, marks: list[int]) -> None:
        """Initialize student object.

        Args:
            name (str): Student name.
            marks (list[int]): List of marks.
        """
        self.name: str = name
        self.marks: list[int] = marks

    def average(self) -> float:
        """Calculate average marks.

        Returns:
            float: Average score.
        """
        return sum(self.marks) / len(self.marks)


def print_data(data: Any) -> None:
    """Print any type of data.

    Args:
        data (Any): Any input data.
    """
    print(data)


def detect_anomaly(values: list[float]) -> list[int]:
    """Detect anomalies based on a threshold.

    Args:
        values (list[float]): Input numeric values.

    Returns:
        list[int]: -1 for anomaly, 1 for normal.
    """
    result: list[int] = []

    for v in values:
        if v > 100:
            result.append(-1)
        else:
            result.append(1)

    return result


def main() -> None:
    """Main function to execute program."""
    nums: list[int] = [10, 20, 30]

    print(add(2, 3))
    print(calculate_average(nums))
    print(count_words("hello world hello"))

    user = find_user(1)
    print(user)

    student = Student("Bhavith", [80, 90, 85])
    print(student.average())

    print(detect_anomaly([50.0, 120.5, 80.0]))


if __name__ == "__main__":
    main()
