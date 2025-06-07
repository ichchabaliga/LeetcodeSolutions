# Last updated: 06/06/2025, 21:22:36
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_array=[[1]*n for _ in range(m)]
        for col in range(1,m):
            for row in range(1,n):
                dp_array[col][row]=dp_array[col-1][row]+dp_array[col][row-1]
        return dp_array[-1][-1]

        