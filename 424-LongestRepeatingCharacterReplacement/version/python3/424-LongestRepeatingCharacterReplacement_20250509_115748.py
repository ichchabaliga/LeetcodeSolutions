# Last updated: 09/05/2025, 11:57:48
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_frequency={}
        start=0
        maxFreq=0
        maxLength=0

        for end,char in enumerate(s):
            char_frequency[char]=char_frequency.get(char,0)+1
            maxFreq=max(maxFreq,char_frequency[char])
            if (end-start+1)-maxFreq>k:
                char_frequency[s[start]]-=1
                start+=1
            maxLength=max(maxLength,end-start+1)
        return maxLength

