class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = prev2 = 0
        for i in range(2, len(cost)+1):
            mcost = min(prev1 + cost[i-1], prev2+cost[i-2])
            prev1, prev2 = mcost, prev1
        return prev1