"""
Problem Statement:

Given a string s and a string t, find the minimum window in s which will contain all the characters in t with the same frequency. If there is no such window in s that covers all characters in t, return an empty string "".
Example:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" contains all characters from "ABC" with required frequencies.

"""


def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # Dictionary to keep count of characters in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    required = len(dict_t)  # Number of unique characters in t

    # Left and right pointers
    l, r = 0, 0
    formed = 0  # Number of unique chars in current window with desired frequency

    # Dictionary to keep count of characters in current window
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):
        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # Check if frequency of current character matches the desired count in t
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try to contract the window until it ceases to be 'desirable'
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # Remove character from the left of the window
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1

    # Return the smallest window or empty string if no valid window
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
