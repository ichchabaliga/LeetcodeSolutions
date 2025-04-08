# Last updated: 08/04/2025, 16:44:42
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        sum_left=0
        # left_sum=sum-right-ele
        for idx,i in enumerate(nums):
            if sum_left==(S-sum_left-i):
                return idx
            sum_left+=i
        return -1



        