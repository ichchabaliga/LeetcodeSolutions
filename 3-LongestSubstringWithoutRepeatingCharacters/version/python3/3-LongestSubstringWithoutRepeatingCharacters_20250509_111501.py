# Last updated: 09/05/2025, 11:15:01
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        start = 0  # Start index of the current window

        for end, char in enumerate(s):
            # If the character is already in the window, move the start pointer
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            # Update the last seen index of the character
            last_seen[char] = end
            # Update the max_length if we found a longer substring
            max_length = max(max_length, end - start + 1)

        return max_length




