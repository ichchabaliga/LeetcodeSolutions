# Last updated: 03/05/2025, 19:09:42
# count number of fresh oranges then bfs while q and count>0
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=0
        queue=deque()
        rows,cols=len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append([r,c])
                elif grid[r][c]==1:
                    count+=1
        print(count,queue)

        def addCell(r,c):
            nonlocal count
            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1):
                return 
            queue.append([r,c])
            grid[r][c]=2
            count-=1
            

        minute=0
        while queue and count>0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            minute+=1
            print(count)

        return minute if count==0 else -1
        