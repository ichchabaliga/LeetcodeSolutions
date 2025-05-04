# Last updated: 03/05/2025, 20:40:04
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pac,atl=set(),set()

        
        def dfs(r,c,ocean,lastheight):
            if r<0 or c<0 or c>=cols or r>=rows or (r,c) in ocean or heights[r][c]<lastheight:
                return
            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])




        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        result=[]
        for i in range(rows):
            for j in range(cols):
                if (i,j) in atl and (i,j) in pac:
                    result.append([i,j])

        return result