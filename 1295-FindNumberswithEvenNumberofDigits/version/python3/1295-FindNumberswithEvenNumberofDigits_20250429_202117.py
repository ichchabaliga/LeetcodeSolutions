# Last updated: 29/04/2025, 20:21:17
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if len(str(num))%2==0:
                count+=1
        return count
        