# Last updated: 28/04/2025, 18:57:54
# Is it better to add the new element on the currSum or start a new subArray?
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSubarray=maxSubarray=nums[0]
        for i in range(1,len(nums)):
            currSubarray=max(currSubarray+nums[i],nums[i] )
            maxSubarray=max(maxSubarray,currSubarray)
        return maxSubarray
        