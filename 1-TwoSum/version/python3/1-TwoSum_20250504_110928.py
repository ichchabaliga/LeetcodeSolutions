# Last updated: 04/05/2025, 11:09:28
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={num:i for i, num in enumerate(nums)}
        
        for i in range(len(nums)):
            if target-nums[i] in hashmap and hashmap[target-nums[i]]!=i:
                return [i,hashmap[target-nums[i]]]


        