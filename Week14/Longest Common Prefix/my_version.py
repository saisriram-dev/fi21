def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]

    count = 0
    for i in range(len(first)):
        if first[i] == last[i]:
            count += 1
        else:
            break
    
    return first[:count]
    