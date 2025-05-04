# Last updated: 04/05/2025, 11:27:52
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high=0,len(numbers)-1
        while low<high:
            numSum=numbers[low]+numbers[high]
            if numSum==target:
                return [low+1,high+1]
            elif numSum<target:
                low+=1
            else:
                high-=1
        return [-1,-1]