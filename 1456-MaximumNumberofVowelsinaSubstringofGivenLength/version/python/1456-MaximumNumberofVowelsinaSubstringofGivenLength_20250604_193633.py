# Last updated: 04/06/2025, 19:36:33
class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        start,end=0,k-1
        vowels='aeiou'
        count=0 
        for i in range(k):
            count+=int(s[i] in vowels)
        answer=count
        for i in range(k,len(s)):
            count+=int(s[i] in vowels) 
            count-=int(s[i-k] in vowels)
            answer=max(answer,count)
        return answer

    

        