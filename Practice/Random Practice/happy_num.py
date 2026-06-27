def is_happy(n: int) -> bool:
    """LeetCode 202: Happy Number
    For non-happy numbers, the sequence will never reach 1,
    and instead will loop endlessly in a cycle that does not include 1.
    To determine if a number is happy, we can use a set to keep track of the numbers
    we have seen in the sequence.

    Eg. 19 is a happy number, because the sequence is:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
    """
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1
