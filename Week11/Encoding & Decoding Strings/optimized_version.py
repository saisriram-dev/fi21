def encode(strs):
    encoded_string = ''

    for word in strs:
        encoded_string += str(len(word)) + '#' + word

    return encoded_string

def decode(s: str):
    i = 0
    res = []

    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1

        length = s[i: j]
        start = j + 1
        stop = j + int(length) + 1

        word = s[start : stop]
        res.append(word)

        i = stop
    
    return res
