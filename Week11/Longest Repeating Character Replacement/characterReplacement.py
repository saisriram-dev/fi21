class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}          # Tracks counts ONLY inside the current window
        i = 0              # Left pointer (window shrinker)
        max_length = 0     # Records our longest valid window
        max_freq = 0       # Tracks the count of the local majority leader

        for j in range(len(s)):
            # 1. EXPAND: Add the incoming character to our window's tracker
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            # Update our majority leader's count if this character just took the lead
            max_freq = max(max_freq, freq[s[j]])

            # 2. CHECK BUDGET: Calculate the rebels
            # Rebels = Total Window Length - Majority Leader Count
            while (j - i + 1) - max_freq > k:
                # Budget blown! Evict the leftmost character from our frequency map
                freq[s[i]] -= 1
                # Shrink the window
                i += 1
            
            # 3. RECORD: The window is now guaranteed to be within budget
            max_length = max(max_length, j - i + 1)
            
        return max_length
    