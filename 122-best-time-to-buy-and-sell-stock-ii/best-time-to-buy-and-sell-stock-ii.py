class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if (profit > 0):
                total += profit
            l = r
            r += 1
        return total

        

