def isPalindrome(s):
    s = s.lower()
    t = ""

    for char in s:
        if char.isalnum():
            t += char

    return t == t[::-1]
