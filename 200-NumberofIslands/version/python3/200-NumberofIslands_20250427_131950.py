# Last updated: 27/04/2025, 13:19:50
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visit=set()
        noOfIslands=0

        def bfs(r,c):
            visit.add((r,c))
            q=deque()
            q.append((r,c))
            directions=[[0,1],[0,-1],[-1,0],[1,0]]
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if (r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]=="1" ):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    noOfIslands+=1
        return noOfIslands



        
        