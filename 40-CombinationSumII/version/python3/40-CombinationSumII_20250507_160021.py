# Last updated: 07/05/2025, 16:00:21
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res=[]
        # candidates.sort()
        # def dfs(index,curr,total):
        #     if index==len(candidates) or total>target:
        #         return
        #     if total==target:
        #         res.append(curr.copy())
        #         return
            
        #     curr.append(candidates[index])
        #     dfs(index+1,curr,total+candidates[index])
        #     curr.pop()
        #     while index+1 <len(candidates) and candidates[index+1]==candidates[index]:
        #         index+=1
            
        #     dfs(index+1,curr,total)

        # dfs(0,[],0)
        # return res     

        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res