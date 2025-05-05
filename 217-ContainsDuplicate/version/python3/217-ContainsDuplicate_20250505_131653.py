# Last updated: 05/05/2025, 13:16:53
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter=Counter(nums)
        for i in counter.values():
            if i>1:
                return True
        return False
        