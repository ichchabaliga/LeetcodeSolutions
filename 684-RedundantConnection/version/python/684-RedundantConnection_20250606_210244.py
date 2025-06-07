# Last updated: 06/06/2025, 21:02:44
# Earn trust
class UnionFind:
    def __init__(self,N):
        self.parent=[i for i in range(N)]
        self.rank=[1]* N
        self.N = N
    
    def find(self,X):
        if X!=self.parent[X]:
            self.parent[X]=self.find(self.parent[X])
        return self.parent[X]
    
    def union(self,X,Y):
        rootX=self.find(X)
        rootY=self.find(Y)
        if rootX==rootY:
            return 
        if self.rank[rootX]>self.rank[rootY]:
            self.parent[rootY]=rootX
            self.rank[rootX]+=self.rank[rootY]
        else:
            self.parent[rootX]=rootY
            self.rank[rootY]+=self.rank[rootX]
        return True





class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N=len(edges)
        uf=UnionFind(N)
        for e in edges:
            if not uf.union(e[0]-1,e[1]-1):
                return e
        return []

        