# Last updated: 29/04/2025, 12:52:59
# Sliding window
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle=max(nums)
        left,count,times=0,0,0
        for right in range(len(nums)):
            if nums[right]==maxEle:
                times+=1
            while times==k:
                
                if nums[left]==maxEle:
                    times-=1
                left+=1
            count+=left
        return count
                



