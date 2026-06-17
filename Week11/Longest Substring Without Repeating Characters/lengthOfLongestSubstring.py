def lengthOfLongestSubstring(s):
    i = 0
    j = 0
    max_window = 0
    seen = set()

    while j < len(s):
        while s[j] in seen:
            seen.remove(s[i])
            i += 1
        
        seen.add(s[j])
        max_window = max(max_window, j - i + 1)
        
        j += 1
    
    return max_window
