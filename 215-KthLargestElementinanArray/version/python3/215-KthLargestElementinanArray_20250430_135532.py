# Last updated: 30/04/2025, 13:55:32
# do a minHeap return len(nums)-k
import random
class Solution:
    # nums = [3,2,3,1,2,4,5,5,6], k = 4
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return nums[0]
