# Last updated: 28/04/2025, 15:49:53
from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_count = Counter(s)
        n = len(s)

        # Check if we have enough characters
        for ch in 'abc':
            if total_count[ch] < k:
                return -1

        window_count = Counter()
        left, max_window = 0, 0

        # Find the longest window that leaves at least k of each character outside
        for right, ch in enumerate(s):
            window_count[ch] += 1

            # Shrink window if we take too many characters
            while left <= right:
                enough_left = all(total_count[c] - window_count[c] >= k for c in 'abc')
                if enough_left:
                    break
                window_count[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return n - max_window