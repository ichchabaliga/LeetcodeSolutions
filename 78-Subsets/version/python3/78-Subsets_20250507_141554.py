# Last updated: 07/05/2025, 14:15:54
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[]
        subset=[]
        def dfs(index):
            if index==len(nums):
                res.append(subset.copy())
                return

            # add element and do next dfs
            subset.append(nums[index])
            dfs(index+1)

            subset.pop()
            dfs(index+1)

        dfs(0)
        return res


        