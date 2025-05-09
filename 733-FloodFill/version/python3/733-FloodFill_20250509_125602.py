# Last updated: 09/05/2025, 12:56:02
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialcolor=image[sr][sc]
        ROWS,COLS=len(image),len(image[0])
        if initialcolor == color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or image[r][c]!=initialcolor:
                return 
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image
        