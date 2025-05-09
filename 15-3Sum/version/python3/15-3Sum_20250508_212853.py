# Last updated: 08/05/2025, 21:28:53
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def twopointersum(index):
            lo,hi=index+1,len(nums)-1
            while lo<hi:
                sumofthree=nums[index] +nums[lo]+nums[hi] 
                if sumofthree<0:
                    lo+=1
                elif sumofthree>0:
                    hi-=1
                else:
                    res.append([nums[index],nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+=1



        for i in range(len(nums)):
            if nums[i] >0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                twopointersum(i)
        return res