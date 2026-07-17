class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit, left, right = 0, 0, 1
        while right <= len(prices) - 1:
            if prices[right] - prices[left] <= 0 :
                left = right
            if prices[right] - prices[left] > profit :
                profit = prices[right] - prices[left]
            right += 1
        return profit
        