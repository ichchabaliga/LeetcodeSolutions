# Last updated: 30/04/2025, 13:35:11
# push (distance,poin)t in the heap
from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[ ((point[0]**2 + point[1]**2) , point) for point in points]
        heapify(minHeap)
        result=[]
        for i in range(k):
            result.append(heappop(minHeap)[1])
        return result