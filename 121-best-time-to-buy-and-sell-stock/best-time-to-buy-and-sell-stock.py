class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf') 
        maxPrice = 0

        for i in range(len(prices)):
            if (prices[i] < low):
                low = prices[i]
            elif (prices[i] - low > maxPrice):
                maxPrice = prices[i] - low
        return maxPrice