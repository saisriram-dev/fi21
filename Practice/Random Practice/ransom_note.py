def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    count = [0] * 26

    for ch in magazine:
        count[ord(ch) - ord('a')] += 1

    for ch in ransomNote:
        if count[ord(ch) - ord('a')] == 0:
            return False
        count[ord(ch) - ord('a')] -= 1

    return True