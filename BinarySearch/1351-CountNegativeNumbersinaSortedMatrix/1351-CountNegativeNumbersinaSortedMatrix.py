class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid[0])
        for row in grid:
            lo,hi=0,n-1
            while lo<=hi:
                mid=(lo+hi)//2
                if row[mid]<0:
                    hi=mid-1
                else:
                    lo=mid+1
            count+=(n-lo)
        return count

        