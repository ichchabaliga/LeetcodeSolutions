# Last updated: 30/04/2025, 19:51:08
# Dynamic programming
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def maximiseDifference(left,right):
            if left==right:
                return nums[left]
            leftScore= nums[left]- maximiseDifference(left+1,right)
            rightScore= nums[right]- maximiseDifference(left,right-1)
            return max(leftScore,rightScore)
        
        return maximiseDifference(0,len(nums)-1) >= 0

        