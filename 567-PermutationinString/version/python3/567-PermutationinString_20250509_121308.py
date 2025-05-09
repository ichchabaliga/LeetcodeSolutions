# Last updated: 09/05/2025, 12:13:08
class Solution:
    from collections import Counter

    def checkInclusion(self, s1, s2):
        # Edge case: s1 longer than s2 cannot be a substring
        if len(s1) > len(s2):
            return False

        # Count characters in s1 and in the first window of s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        # If the first window matches, return True
        if s1_count == window_count:
            return True

        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            # Character going out of the window
            char_out = s2[i - len(s1)]
            # Character coming into the window
            char_in = s2[i]

            # Decrease count for outgoing character
            window_count[char_out] -= 1
            # Remove the character from the counter if its count is zero
            if window_count[char_out] == 0:
                del window_count[char_out]

            # Increase count for incoming character
            window_count[char_in] += 1

            # Compare window with s1's count
            if window_count == s1_count:
                return True

        # No permutation found
        return False
