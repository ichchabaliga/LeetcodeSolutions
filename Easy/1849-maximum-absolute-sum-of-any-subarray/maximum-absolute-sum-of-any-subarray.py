class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)

        return max_sum - min_sum