# Last updated: 30/04/2025, 12:54:03
# Maintain a fixed sized Heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap=[]
        self.k=k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.minHeap)<self.k or self.minHeap[0]<val:
            heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)