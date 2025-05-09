# Last updated: 08/05/2025, 21:43:05
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        left,right=0,len(height)-1
        while left<right:
            maxarea=max(maxarea,min(height[left], height[right])*(right-left))
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxarea


        