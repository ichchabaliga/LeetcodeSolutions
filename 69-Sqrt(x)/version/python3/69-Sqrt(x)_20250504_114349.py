# Last updated: 04/05/2025, 11:43:49
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low,high=2,x//2
        while low<=high:
            mid=(low+high)//2
            
            if mid*mid<x:
                low=mid+1
            elif mid*mid>x:
                high=mid-1
            else:
                return mid
        return high

        