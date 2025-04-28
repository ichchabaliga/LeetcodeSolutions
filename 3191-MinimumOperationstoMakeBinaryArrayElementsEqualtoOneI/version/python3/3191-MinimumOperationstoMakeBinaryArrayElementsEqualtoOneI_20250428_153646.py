# Last updated: 28/04/2025, 15:36:46
# Sliding window of length 3
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]=1
                
                nums[i+1]= nums[i+1]^1
                nums[i+2]= nums[i+2]^1
                count+=1
        if sum(nums)!=len(nums):
            return -1
        return count


        