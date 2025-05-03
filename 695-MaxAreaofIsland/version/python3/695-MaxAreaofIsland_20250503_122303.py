# Last updated: 03/05/2025, 12:23:03
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lenRow=len(grid)
        lenCol=len(grid[0])
        visited=set()
        max_area=0
        def dfs(row,col):
            if (row<0 or col<0 or row>=lenRow or col>=lenCol or (row,col) in visited or grid[row][col]==0):
                return 0

            visited.add((row,col))
            
            return (1+dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1))
        for i in range(lenRow):
            for j in range(lenCol):
                if grid[i][j]==1 and (i,j) not in visited:
                    curr_area=dfs(i,j)
                    max_area=max(max_area,curr_area)
        return max_area
