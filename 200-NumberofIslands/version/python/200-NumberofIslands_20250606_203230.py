# Last updated: 06/06/2025, 20:32:30
class Solution:
    def dfs(self, arr, i, j, m,n):
        self.hash_map[(i,j)] = self.count
        sides = [(i+1, j),(i-1, j),(i, j-1),(i, j+1)]
        for (x,y) in sides:
            if x < 0 or y <0 or x >= m or y >= n:
                continue
            if arr[x][y] == '1' and (x,y) not in self.hash_map:
                self.dfs(arr, x, y, m,n)

    def numIslands(self, arr):
        self.count = 0
        self.hash_map = {}
        m = len(arr)
        if m == 0:
            return 0
        n = len(arr[0])
        for i in range(m):
            for j in range(n):
                if arr[i][j] == '0':
                    continue
                else:
                    if not (i,j) in self.hash_map:
                        self.count += 1
                        self.dfs(arr, i, j, m, n)
        print(self.hash_map)
        return len(set(self.hash_map.values()))
