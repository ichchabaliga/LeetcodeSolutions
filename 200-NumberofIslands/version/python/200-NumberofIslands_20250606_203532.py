# Last updated: 06/06/2025, 20:35:32
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         Rows=len(grid)
#         Cols=len(grid[0])
#         number_of_islands=0

#         def dfs(row,col):
#             if ( row<0 or col<0 or row>=Rows or col>=Cols or grid[row][col]=='0'):
#                 return 
#             grid[row][col]='0'
#             dfs(row+1,col)
#             dfs(row-1,col)
#             dfs(row,col+1)
#             dfs(row,col-1)

#         for i in range(Rows):
#             for j in range(Cols):
#                 if grid[i][j]=='1': 
#                     dfs(i,j)
#                     number_of_islands+=1
                    
#         return number_of_islands
                    




# Union Find
class UnionFind:
    def __init__(self,grid):
        self.count=0
        row, col=len(grid), len(grid[0])
        self.parent=[]
        self.rank=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':

                    self.parent.append(i*col+j)
                    self.count+=1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
        

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX==rootY:
            return #they belong to the same set
        if self.rank[rootX]>self.rank[rootY]:
            self.parent[rootY]=rootX
        elif self.rank[rootX]<self.rank[rootY]:
            self.parent[rootX]=rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.count-=1
    
    def getCount(self):
        return self.count
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        uf = UnionFind(grid)
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    grid[r][c]="0"
                    if r-1>=0 and grid[r - 1][c] == "1":
                        uf.union(r*col+c,(r-1)*col+c)
                    if r+1<row and grid[r + 1][c] == "1":
                        uf.union(r*col+c,(r+1)*col+c)
                    
                    if c-1>=0 and grid[r][c-1] == "1":
                        uf.union(r*col+c,r*col+(c-1))
                    if c+1<col and grid[r][c+1] == "1":
                        uf.union(r*col+c,r*col+(c+1))
        return uf.getCount()