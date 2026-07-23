class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            if prices[r] - prices[l] >= 0:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            r += 1
        return maxProfit
