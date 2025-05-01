# Last updated: 30/04/2025, 20:14:50
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        minHeap=[(matrix[i][0],i,0) for i in range(n)]
        heapify(minHeap)

        while k:
            element,row,col=heappop(minHeap)
            k-=1
            if col< n-1:
                heappush(minHeap,(matrix[row][col+1],row,col+1))

        return element
