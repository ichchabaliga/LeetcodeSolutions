class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        result=[]
        for i in candies:
            result.append((i + extraCandies) >=maxCandies)
        
        return result


        