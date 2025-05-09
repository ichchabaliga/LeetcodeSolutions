# Last updated: 09/05/2025, 12:32:07
class Solution:
    from collections import Counter

    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        
        s1Freq=Counter(s1)
        windowFreq=Counter(s2[:len(s1)])
        
        if s1Freq==windowFreq:
            return True
        
        for i in range(len(s1),len(s2)):
            char_out=s2[i-len(s1)]
            char_in=s2[i]
            windowFreq[char_in]+=1
            windowFreq[char_out]-=1
            if windowFreq[char_out]==0:
                del windowFreq[char_out]
            if s1Freq==windowFreq:
                return True

        return False