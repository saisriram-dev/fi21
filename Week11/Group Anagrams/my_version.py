def groupAnagrams(strs):

    seen = {}

    def count(string):
        freq = {}

        for ch in string:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Dictionary is not hashable, so we convert it to a tuple of sorted items
        # Hashable means that it can be used as a key in a dictionary or stored in a set.
        return tuple(sorted(freq.items()))
    
    for word in strs:
        key = count(word)

        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]
        
    return list(seen.values())

"""
Time complexity: O(N * K log K), 
where N is the number of strings, K is the maximum length of a string. 

return tuple(sorted(freq.items())) 
The above line sorts the items of the frequency dictionary, which takes O(K log K) time
and we do this for each of the N strings, resulting in O(N * K log K) time complexity.
"""
