// Last updated: 19/03/2025, 18:40:54
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo,hi=1,n
        while(lo<hi):
            mid=lo+(hi-lo)/2
            if(isBadVersion(mid)):
                hi=mid
            else:
                lo=mid+1
        return int(lo)

        