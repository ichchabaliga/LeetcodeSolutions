# Last updated: 05/05/2025, 13:21:54
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS=Counter(s)
        countT=Counter(t)
        for i in s:
            if not i in t or countT[i]!=countS[i]:
                return False
        return True

        