from collections import Counter


def checkInclusion(s1, s2):
    count1 = Counter(s1)

    i = 0
    j = len(s1)

    while j <= len(s2):
        if count1 == Counter(s2[i: j]):
            return True
        else:
            i += 1
            j += 1
    
    return False
