# Last updated: 03/05/2025, 11:11:19
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        lenCol=len(grid[0])
        lenRow=len(grid)
        numIsland=0
        def dfs(row,col):
            if (row<0 or col<0 or col>=lenCol or row>=lenRow or grid[row][col]!="1"):
                return 
            grid[row][col]=0  #visited
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    numIsland+=1

        return numIsland

        
        