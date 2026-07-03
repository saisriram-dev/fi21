def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    first, last = strs[0], strs[-1]
    
    result = []
    # zip pairs the characters together: ('f', 'z'), ('l', 'z')...
    # it automatically stops at the end of the shorter string
    for c1, c2 in zip(first, last):
        if c1 == c2:
            result.append(c1)
        else:
            break
    
    return "".join(result)
