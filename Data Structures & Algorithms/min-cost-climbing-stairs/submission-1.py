class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m1 = m2 = 0
        for i in range(2, len(cost)+1):
            mc = min(m1 + cost[i-1], m2 + cost[i-2])
            m1, m2 = mc, m1
        return m1

