# Last updated: 09/05/2025, 11:42:04
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_frequency = {}
        max_length = 0
        max_repeat_count = 0  # Count of the most frequent character in the current window
        start = 0

        for end in range(len(s)):
            right_char = s[end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

            # Update max_repeat_count if this character's frequency is higher
            max_repeat_count = max(max_repeat_count, char_frequency[right_char])

            # Current window size is end - start + 1
            # Number of chars to replace = window size - max_repeat_count
            if (end - start + 1) - max_repeat_count > k:
                # Shrink the window from the left
                left_char = s[start]
                char_frequency[left_char] -= 1
                start += 1

            # Update max_length if the current window is larger
            max_length = max(max_length, end - start + 1)

        return max_length