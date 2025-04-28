# Last updated: 28/04/2025, 11:43:33
# Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=float("inf")
        maxProfit=0
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
            elif maxProfit<prices[i]-minPrice:
                maxProfit=max(maxProfit,prices[i]-minPrice)
        return maxProfit
        