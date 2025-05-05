# Last updated: 05/05/2025, 13:26:02
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS=[0]*26
        countT=[0]*26
        for i in range(len(s)):
            countS[ord(s[i])-ord('a')]+=1
            countT[ord(t[i])-ord('a')]+=1
        if tuple(countS)!=tuple(countT):
            return False
            
        return True

        