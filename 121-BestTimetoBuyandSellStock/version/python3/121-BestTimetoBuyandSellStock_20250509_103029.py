# Last updated: 09/05/2025, 10:30:29
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,high=0,1
        maxProfit=0
        while high<len(prices):
            if prices[low]<prices[high]:
                maxProfit=max(maxProfit,(prices[high]-prices[low]))
              
            else:
                low=high
            high+=1
        return maxProfit
            
            

        