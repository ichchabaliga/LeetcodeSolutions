# Last updated: 28/04/2025, 14:20:19
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=Counter()
        left,right=0,0
        result=0
        while right<len(s):
            r=s[right]
            chars[r]+=1
            while chars[r]>1:
                l=s[left]
                chars[l]-=1
                left+=1
            result=max(result,right-left+1)
            right+=1
        return result


        
        