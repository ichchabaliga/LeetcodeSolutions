# Last updated: 20/05/2025, 20:02:15
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
       
        if len(trust)<n-1:
            return -1
        trust_score=[0]*(n+1)
        for i,j in trust:
            trust_score[i]-=1
            trust_score[j]+=1
        for i,score in enumerate(trust_score[1:],1):
            if score==n-1:
                return i
        return -1 
        