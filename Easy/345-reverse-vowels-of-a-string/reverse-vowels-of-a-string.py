class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            if c.lower() in 'aeiou':
                return True

            else: return False
        
        # Using 2 pointer approach, if start<end, swap left and right
        start=0
        end=len(s)-1
        s = list(s)
        while start<end:
            while start < len(s) and not isVowel(s[start]):
                start += 1
        # Find the rightmost vowel
            while end >= 0 and not isVowel(s[end]):
                end -= 1

            if start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)
