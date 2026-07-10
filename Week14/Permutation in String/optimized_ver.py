from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)

    if n > m:
        return False

    target = Counter(s1)
    window = Counter(s2[:n])

    if window == target:
        return True

    for i in range(n, m):
        # Add the new character
        window[s2[i]] += 1

        # Remove the old character
        window[s2[i - n]] -= 1

        # Remove the key if its count becomes 0
        if window[s2[i - n]] == 0:
            del window[s2[i - n]]

        if window == target:
            return True

    return False
