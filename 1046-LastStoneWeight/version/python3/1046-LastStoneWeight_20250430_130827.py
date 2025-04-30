# Last updated: 30/04/2025, 13:08:27
# pop pop subtract push
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-s for s in stones]
        heapify( maxHeap)

        while len(maxHeap)>=2:
            stone1=heapq.heappop(maxHeap)
            stone2=heapq.heappop(maxHeap)
            stoneLeft=abs(stone1-stone2)
            if stoneLeft >0:
                heapq.heappush(maxHeap,-stoneLeft)
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0

        