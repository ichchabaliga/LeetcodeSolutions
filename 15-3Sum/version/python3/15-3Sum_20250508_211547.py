# Last updated: 08/05/2025, 21:15:47
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def twosum(i):
            left=i+1
            right=len(nums)-1
            while left<right:
                sums=nums[left]+nums[i]+nums[right]
                if sums<0:
                    left+=1
                elif sums>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                twosum(i)

        return res
