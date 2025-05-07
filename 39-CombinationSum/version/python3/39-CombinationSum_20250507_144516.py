# Last updated: 07/05/2025, 14:45:16
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(index,total,currList):
            if index>=len(candidates) or total>target:
                return 
            if total==target:
                res.append(currList.copy())
                return

            currList.append(candidates[index] )
            sumCurr=total+candidates[index]   
            dfs(index,sumCurr,currList) 

            currList.pop()
            dfs(index+1,total,currList)

        dfs(0,0,[])
        return res    