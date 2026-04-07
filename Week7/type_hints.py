# a: (type) means, "a is expected to be of this type"
# Eg. def add(a: int, b: int) -> int:
# The -> int means the function is expected to return an int.

from typing import Any


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def calculate_average(nums: list[int]) -> float:
    """Calculate average of a list."""
    return sum(nums) / len(nums)


def count_words(text: str) -> dict[str, int]:
    """Count frequency of each word."""
    words = text.split()
    freq: dict[str, int] = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def find_user(user_id: int) -> str | None:
    """Return username or None if not found."""
    users = {1: "Alice", 2: "Bob"}

    return users.get(user_id)


class Student:
    def __init__(self, name: str, marks: list[int]) -> None:
        self.name: str = name
        self.marks: list[int] = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)


def print_data(data: Any) -> None:
    """Print any type of data."""
    print(data)


def detect_anomaly(values: list[float]) -> list[int]:
    """
    Detect anomalies using a simple threshold.

    Returns:
        list[int]: -1 for anomaly, 1 for normal
    """
    result: list[int] = []

    for v in values:
        if v > 100:
            result.append(-1)
        else:
            result.append(1)

    return result


def main() -> None:
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
