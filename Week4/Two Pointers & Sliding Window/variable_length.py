# Variable length Sliding window algorithm
# In this technique, we use two pointers to represent a window that can expand and contract as needed.

""" This technique is useful with data structures like arrays, strings, and linked lists. 
    It is often used to solve problems that involve finding a contiguous subarray or 
    substring that satisfies certain conditions. """

# To find the length of the longest substring without repeating characters in a given string, 
# we can use the variable length sliding window technique.

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    longest = 0
    n = len(s)

    for r in range(n):
        while s[r] in char_set:
            char_set.remove(s[left])
            left += 1

        w = (r - left) + 1 # Calculate the current window size
        longest = max(longest, w)
        char_set.add(s[r])
    
    return longest
