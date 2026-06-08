from collections import defaultdict

def groupAnagrams(strs):
    seen = defaultdict(list)

    for word in strs:
        spaces = [0] * 26

        for ch in word:
            spaces[ord(ch) - ord('a')] += 1
        
        track = tuple(spaces)
        seen[track].append(word)
    
    return list(seen.values())

"""
Sorting problem is eliminated when compared to my version as we are using a fixed size of list (26)
everytime, which is O(1) time complexity for each word. Byt in my_version.py, 
we are sorting the frequency dictionary for each word, which takes O(K log K) time.

Also ASCII:
    If we subtract the ASCII value of 'a' from the ASCII value of the character, 
    we get a number between 0 and 25, which corresponds to the index of the character.

    For eg. ord('a') = 97, ord('e') = 101, so ord('e') - ord('a') = 4, 
    which means 'e' corresponds to index 4 (or position 5) in the spaces list.

So as sorting is eliminated,
the time complexity of this optimized version is O(N * K), 
where N is the number of strings and K is the maximum length of a string.
"""
