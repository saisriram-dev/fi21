def decodeString(s):
    stack = []
    current_num = 0
    current_str = ""

    for ch in s:

        if ch.isdigit():
            current_num = current_num * 10 + int(ch)

        elif ch == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0

        elif ch == "]":
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str

        else:
            current_str += ch

    return current_str


# Example usage:
s = "3[a]2[bc]"
print(decodeString(s))  # Output: "aaabcbc"
s = "3[a2[c]]"
print(decodeString(s))  # Output: "accaccacc"
s = "2[abc]3[cd]ef"
print(decodeString(s))  # Output: "abcabccdcdcdef"
