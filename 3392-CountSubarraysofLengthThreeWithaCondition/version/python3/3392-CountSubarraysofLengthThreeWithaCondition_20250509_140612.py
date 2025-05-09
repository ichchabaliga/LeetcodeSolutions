# Last updated: 09/05/2025, 14:06:12
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        count=0
        if len(nums)<3:
            return 0

        for i in range(1,len(nums)-1):
            if nums[i]==(nums[i-1]+nums[i+1])*2 :
                count+=1

        return count




        